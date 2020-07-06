import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required
from data.user import User
from pprint import pprint
import json
from security import encrypt_password, check_encrypted_password

class UserModel():
    
    def __init__(self, _id, email, username, password, role):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password
        self.role = role

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
            user.role = login_user.role
        else:
            user = None
        return user

    def finduser_by_username(username) -> User:
        pprint(username)
        login_user = User.objects(username=username).first()

        retuserdetails = {}        
        if login_user:
            retuserdetails['username'] = login_user.username
            retuserdetails['_id'] = login_user._id
            retuserdetails['email'] = login_user.email
            retuserdetails['role'] = login_user.role
            
        else:
            retuserdetails = None
        return retuserdetails
    
    def finduser_by_user_id(user_id) -> User:
        pprint(user_id)
        login_user = User.objects(_id=user_id).first()
        retuserdetails = {}        
        if login_user:
            retuserdetails['username'] = login_user.username
            retuserdetails['_id'] = login_user._id
            retuserdetails['email'] = login_user.email
            retuserdetails['role'] = login_user.role
            
        else:
            retuserdetails = None
        return retuserdetails

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
            user.role = login_user.role
        else:
            user = None
        return user

   
      
    def register_user(data)  -> User:
        user = User()
        user._id = UserModel.getcounter()
        user.email = data['email']
        user.username = data['username']
        user.password = encrypt_password(data['password'])
        user.role = data['role']
        user.save()
        return user

    def getcounter():
        user = User()
        counter = 1
        firstuser = User.objects().order_by('-_id').first()
        if firstuser:
            counter = (firstuser._id) + 1
            
        return counter
    
    def find_all_users()  -> User:
        user = User()
        queryset = User.objects().order_by('-_id')
        
        user_collection = []
        for user in queryset:
            retuserdetails = {}
            retuserdetails['username'] = user.username
            retuserdetails['_id'] = user._id
            retuserdetails['email'] = user.email
            retuserdetails['role'] = user.role
            user_collection.append(retuserdetails)
        return user_collection
    
    def delete_user(username)  -> User:
        user = User()
        del_user = User.objects(username=username)
        del_user.delete()

        del_user = User.objects(username=username)       
        return del_user
    
    def update_user(data, username)  -> User:
        
        exist_user = User.objects(username=username).first()
        
        if exist_user:
            if data['email']:
                exist_user.email = data['email']
            if data['username']:
                exist_user.username = data['username']
            if data['password']:
                    exist_user.password = encrypt_password(data['password'])
            if data['role']:
                exist_user.role = data['role']
                   
            updated_user = exist_user.save()
            return updated_user

        return exist_user