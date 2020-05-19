from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.company
    db.cars.drop()
    db.developers.drop()
