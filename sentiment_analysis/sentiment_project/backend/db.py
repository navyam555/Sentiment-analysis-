from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_db"]
collection = db["reviews"]

def save_data(data):
    collection.insert_one(data)