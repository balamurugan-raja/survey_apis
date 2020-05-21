import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required



class UserModel():
    client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
    userdb = client["User"]
    userlist = userdb["userlist"]

    def __init__(self, _id, email, username, password):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        pprint(username)
        client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
        userdb = client["User"]
        userlist = userdb["userlist"]
        login_user = userlist.find_one({'username' : username})
        if login_user:
            user = cls             
            user.username = login_user['username']
            user.password = login_user['password']
            user.email = login_user['email']
            user.id = login_user['_id']
            
            pprint(user.username)
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
        userdb = client["User"]
        userlist = userdb["userlist"]
        login_user = userlist.find_one({'_id' : _id})
        if login_user:
            user = cls
            user.username = login_user['username']
            user.password = login_user['password']
            user.email = login_user['email']
            user.id = login_user['_id']
            pprint(user.username)
        else:
            user = None
        return user