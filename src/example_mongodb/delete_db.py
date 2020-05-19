import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

print("List of databases before deletion\n--------------------------")
for x in client.list_database_names():
    print(x)

# delete database named 'organisation'
client.drop_database('company')

print("\nList of databases after deletion\n--------------------------")
for x in client.list_database_names():
    print(x)
