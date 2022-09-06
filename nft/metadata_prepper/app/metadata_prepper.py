import json
from pathlib import Path
import os
from pymongo import MongoClient
import datetime


def process_files(
        directory: str,
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
                                     collection)
            if processed:
                total_processed += 1
                print(f'Processed: {total_processed} json files')
    return total_processed


def process_file(root: str,
                 name: str,
                 collection):
    #validate file
    path = f'{root}/{name}'
    filepath = os.fsdecode(path)
    filestem = Path(filepath).stem
    if not filepath.endswith(('.json')):
        return False
    else:
        b = os.path.getsize(f'{filepath}')
        B = b / (1 << 20)
        if B > 99:
            raise Exception(f'The file {filepath} is too large: {B}MB')


    #store nft data

    with open(f'{path}', 'rb') as f:
        data = json.load(f)

    upsertable_data = {
        'nft_body': data,
        'nft_body_filestem': filestem,
        'nft_body_added_at': datetime.datetime.utcnow()
    }
    collection.update_one({'image_filestem': filestem}, {"$set": upsertable_data}, upsert=True) #this will update records with a matching image filestem, otherwise it will insert a new record

    # collection.insert_one({'ipfs_uri': f'ipfs://{res.json()["IpfsHash"]}',
    #                        'nft_collection_name': nft_collection_name,
    #                        'image_filename': f'{name}',
    #                        'processed_at': datetime.datetime.utcnow()})


    return True


def run_metadata_prepper(mongo_uri):
    print('Spinning up metadata prepper...')
    mod_path = Path(__file__).parent
    upload_directory = f'{mod_path}/../upload'

    mongo_client = MongoClient(mongo_uri)
    db = mongo_client.blockery_public

    processed_files_count = process_files(upload_directory, db)
    print(f'Total processed json files: {processed_files_count}')


if __name__ == "__main__":
    mongo_uri = os.environ['MONGO_URI']
    run_metadata_prepper(mongo_uri)