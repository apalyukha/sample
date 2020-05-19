from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.company
    print(db.list_collection_names())
