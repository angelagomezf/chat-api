from pymongo import MongoClient

client = MongoClient()
db = client.get_database("chat-api")

def get_chat(name):
    curs = db.chat.find({"name":"name"})
    return list(curs)


def insert_data(collection, data):
    curs = db[collection].insert_one(data)
    return {"_id": curs.inserted_id}