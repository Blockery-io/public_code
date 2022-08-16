import requests
import os
from pymongo import MongoClient
import datetime


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
    nft_collection_name = os.path.basename(root)
    if not filepath.endswith(('.jpg', '.png')):
        return False
    else:
        b = os.path.getsize(f'{filepath}')
        B = b / (1 << 20)
        if B > 99:
            raise Exception(f'The file {filepath} is too large: {B}MB')


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
                           'image_filename': f'{name}',
                           'processed_at': datetime.datetime.utcnow()})


    return True
