import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

for db in client.list_databases():
    print(db)
