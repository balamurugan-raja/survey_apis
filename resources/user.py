import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required




class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
        userdb = client["User"]
        userlist = userdb["userlist"]
        
        usercursor = userlist.find().sort('_id', pymongo.DESCENDING)[0]
        counter = (usercursor['_id']) + 1
        pprint(counter)
        userobj = {'_id':counter, 'email': data['email'], 'username': data['username'], 'password': data['password']}
        userlist.insert(userobj)

        return {"message": "User created successfully."}, 201

class UserArray(Resource):
    @jwt_required()
    def get(self):
        pprint("reached userarray method")
        client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
        userdb = client["User"]
        userlist = userdb["userlist"]
        usercursor = userlist.find()
        userarray = []
        for userobj in usercursor:
                userarray.append({ 'userid': userobj['_id'], 'email': userobj['email'], 'username': userobj['username'], 'password': userobj['password'] })
                pprint(userobj)
        pprint(userarray)
        return userarray