from app.import_nft_data import process_files
import os
from pymongo import MongoClient


def run_metadata_prepper():
    upload_directory = '../upload'

    mongo_client = MongoClient(os.environ['MONGO_URI'])
    db = mongo_client.blockery_public

    processed_images_count = process_files(upload_directory, db)
    print(f'Total processed json files: {processed_images_count}')

if __name__ == "__main__":
    run_metadata_prepper()