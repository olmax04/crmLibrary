import os

from pymongo import MongoClient

token = os.environ.get("MONGO_DB")

client = MongoClient(token)

users = client.parser.users

codes = client.parser.codes

objects = client.parser.objects

api = client.grandrealestate.api