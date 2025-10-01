import os
from dotenv import load_dotenv
from pymongo import MongoClient

DB_NAME   = "sample_supplies"
COLL_NAME = "sales"

def get_collection():
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    return client[DB_NAME][COLL_NAME]
