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
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isdir(full_path):
            continue
        elif os.path.isfile(full_path):
            processed = process_file(full_path,
                                     collection,
                                     pinata_jwt)
            if processed:
                total_processed += 1
                print(f'Processed: {total_processed} images')
        else:
            print(f'Unidentified name {full_path}. It could be a symbolic link')
    return


def process_file(path: str,
                 collection,
                 pinata_jwt: str):
    #validate file
    filepath = os.fsdecode(path)
    filename = os.path.basename(filepath)
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
                            'image_filename': f'{filename}',
                            'processed_at': datetime.datetime.utcnow()})


    return True
