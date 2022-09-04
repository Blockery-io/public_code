from app.upload_images import process_files
import os
from pymongo import MongoClient


def run_pinner(pinata_jwt, mongo_uri):
    upload_directory = '../upload'

    mongo_client = MongoClient(mongo_uri)
    db = mongo_client.blockery_public

    processed_images_count = process_files(upload_directory, pinata_jwt, db)
    print(f'Total processed images: {processed_images_count}')

if __name__ == "__main__":
    pinata_jwt = os.environ['PINATA_API_KEY']
    mongo_uri = os.environ['MONGO_URI']
    run_pinner(pinata_jwt, mongo_uri)