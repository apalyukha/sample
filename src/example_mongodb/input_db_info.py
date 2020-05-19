import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

dbname = input("Enter database name: ")  # company
db = client[dbname]

# list the collections
for coll in db.list_collection_names():
    print(coll)
