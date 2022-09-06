import requests
import os
from pymongo import MongoClient
import datetime
from pathlib import Path


def add_index_if_not_exists(index_name, collection):
    if index_name not in collection.index_information():
        collection.create_index(index_name, unique=True)


def process_files(
        directory: str,
        pinata_jwt: str,
        db: MongoClient
        ):
    """
    Recursively search a
    :param directory:
    :return:
    """
    collection = db.nfts
    add_index_if_not_exists('image_filename', collection)
    add_index_if_not_exists('nft_collection_name', collection)

    total_processed = 0
    print(f'Begin processing files')
    for root, dirs, files in os.walk(directory):
        for name in files:
            print(os.path.join(root, name))
            processed = process_file(root,
                                     name,
                                     collection,
                                     pinata_jwt)
            if processed:
                total_processed += 1
                print(f'Processed: {total_processed} images')
    return total_processed


def process_file(root: str,
                 name: str,
                 collection,
                 pinata_jwt: str):
    #validate file
    path = f'{root}/{name}'
    filepath = os.fsdecode(path)
    filestem = Path(filepath).stem
    nft_collection_name = os.path.basename(root)
    if not filepath.endswith(('.jpg', '.png')):
        return False
    else:
        b = os.path.getsize(f'{filepath}')
        B = b / (1 << 20)
        if B > 99:
            raise Exception(f'The file {filepath} is too large: {B}MB')

    match = collection.find_one({'image_filename': name, 'nft_collection_name': nft_collection_name})
    if match:
        print(f'Entry for file/collection combination already found in database. This was already processed:\n '
              f'\timage_filename: {name}\n'
              f'\tnft_collection_name: {nft_collection_name}')
        return False

    #upload file

    with open(f'{path}', 'rb') as f:
        data = f.read()
    res = requests.post(url='https://api.pinata.cloud/pinning/pinFileToIPFS',
                        files={'file': data},
                        headers={
                            'Authorization': f'Bearer {pinata_jwt}'
                        })
    if not res.ok:
        raise Exception(f'failed to upload to nft_drop storage with error: {res.text}')
    collection.insert_one({'ipfs_uri': f'ipfs://{res.json()["IpfsHash"]}',
                           'nft_collection_name': nft_collection_name,
                           'image_filename': name,
                           'image_filestem': filestem,
                           'image_pinned_at': datetime.datetime.utcnow()})


    return True


def run_pinner(pinata_jwt, mongo_uri):
    print('Image pinner starting up')
    mod_path = Path(__file__).parent
    upload_directory = f'{mod_path}/../upload'

    mongo_client = MongoClient(mongo_uri)
    db = mongo_client.blockery_public


    processed_images_count = process_files(upload_directory, pinata_jwt, db)
    print(f'Total processed images: {processed_images_count}')


if __name__ == "__main__":
    pinata_jwt = os.environ['PINATA_API_KEY']
    mongo_uri = os.environ['MONGO_URI']
    run_pinner(pinata_jwt, mongo_uri)