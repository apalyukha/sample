from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.company
    print(db.list_collection_names())

    status = db.command("dbstats")
    pprint(status)
