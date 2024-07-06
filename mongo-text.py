import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://gary:gary1217@atlascluster.d0ukjd8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db=client.text
collection=db.users
collection.insert_one({
    "name":"gary",
    "gender":"male"
})
print("sussed save")