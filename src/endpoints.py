from src.app import app
from flask import request
from helpers.mongoConnection import *
from bson import json_util
import os
from random import choice



# WELCOME
@app.route("/")
def welcome():
    return {"welcome": "Hi! Welcome to my API"}


# USER ENDPOINTS
@app.route("/user/create/<username>")
def create_user(username):
    print({"username":username})
    return json_util.dumps(insert_user({"username":username}))


# CHAT ENDPOINTS
@app.route("/chat/create/<chatname>")
def insert_chat(chatname):
    users = request.args.getlist("user_id")
    print({"chat name":chatname, "users list":users})
    result = {"chat name":chatname, "users list":users}
    return json_util.dumps(insert_chat(result))


@app.route ("/chat/<chat_id>/addmessage")
def create_message(chat_id):
    user = request.args.get("user_id")
    text = request.args.get("text")
    chat = {"chat_id":chat_id, "user_id":user, "text":text}
    return json_util.dumps(insert_message(chat))