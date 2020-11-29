from app import app
from flask import request, senf_from_direcoty
from mongoConnection import get_chat, insert_data
from bson import json_util
import os
from random import choice


# WELCOME
@app.route("/")
def welcome():
    return {"welcome": "Hi! Welcome to my API"}


# USER ENDPOINTS
@app.route("/user/create/")
def create_user():
    return {"user_id": "username"}


# CHAT ENDPOINTS
@app.route("/chat/create/")
def create_chat():
    return {"chat_id": "chatname"}

@app.route("/chat/adduser/")
def add_user():
    return {"chat_id": "user_id"}

@app.route("/chat/addmessage/")
def add_message():
    return {"message_id": "text"}

@app.route("/chat/list/")
def chat_list():
    return add_message.json()

