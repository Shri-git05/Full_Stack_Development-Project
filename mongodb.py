# speech_app/mongodb.py
from pymongo import MongoClient

def get_mongo_client():
    return MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URL

def save_recognition_result(text, translated_text):
    client = get_mongo_client()
    db = client['speech_db']
    collection = db['results']
    result = {"original_text": text, "translated_text": translated_text}
    collection.insert_one(result)
