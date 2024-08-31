from flask import current_app
from flask_pymongo import PyMongo
from pymongo.errors import ServerSelectionTimeoutError

mongo = PyMongo()

def initialize_db(app):
    mongo.init_app(app)
    try:
        mongo.db.list_collection_names()
        print("connected")
    except ServerSelectionTimeoutError:
        print("Failed to connect to MongoDB!")

def get_db():
    return mongo.db