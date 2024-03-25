from numpy import load
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB.URI"))

db = client["hci"]

collection = db["user-config"]

customGestureJson = collection.find_one({"_id": "3003c80ff73e-Aditya-Victus"})

if customGestureJson == None:
    print("No data found")
else:
    print(customGestureJson)