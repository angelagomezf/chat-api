from pymongo import MongoClient

client = MongoClient()
db = client.get_database("chat-api")

def insert_user(username):
    curs = db.user.insert_one(username)
    return {"_id": curs.inserted_id, "username":1}


def insert_chat(chatname):
    curs = db.chat.insert_one(chatname)
    return {"_id": curs.inserted_id, "chatname":1, "username":1}


def insert_message(message):
    curs = db.messages.insert_one(message)
    return {"_id": curs.inserted_id, "chatname":1, "username":1}
