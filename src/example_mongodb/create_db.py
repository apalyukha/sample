import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# use database named "organisation"
mdb = client["company"]

# use collection named "developers"
coll = mdb["developers"]

# a document
developer = {"name": "dru", "address": "Ukraine"}

# insert a document to the collection
x = coll.insert_one(developer)  # без цієї шляпи бобо

# list the databases
for db in client.list_databases():
    print(db)
