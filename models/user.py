import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required
from data.user import User


class UserModel():
    
    def __init__(self, _id, email, username, password):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username) -> User:
        pprint(username)
        login_user = User.objects(username=username).first()
                
        if login_user:
            user = cls
            user.username = login_user.username
            user.password = login_user.password
            user.email = login_user.email
            user.id = login_user._id
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id) -> User:
        pprint(_id)
        login_user = User.objects(_id=_id).first()

        if login_user:
            user = cls
            user.username = login_user.username
            user.password = login_user.password
            user.email = login_user.email
            user.id = login_user._id
        else:
            user = None
        return user

   
    @classmethod
    def create_user(cls, _id, email, username, password)  -> User:
        user = User()
        user._id =_id
        user.email = email
        user.username = username
        user.password = password

        user.save()
        return user

