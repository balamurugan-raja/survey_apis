import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from flask import Flask, jsonify
from pprint import pprint
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
     jwt_required,
     create_access_token,
     create_refresh_token,
     get_jwt_claims,
     jwt_refresh_token_required,
     get_jwt_identity,
     get_raw_jwt

)
from blacklist import BLACKLIST
from security import encrypt_password, check_encrypted_password



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
    parser.add_argument('role',
                        type=str,
                        required= False,
                        help="This field is optional"
                        )
                        

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.finduser_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        
        created_user = UserModel.register_user(data)
        if created_user:
            return {"message": "User created successfully."}, 201
        else:
            return {"message": "User Not Created."},400

class UserArray(Resource):
    @jwt_required
    def get(self):
        userarray = UserModel.find_all_users()
        if userarray:
            return userarray
        return {'message': 'No users found'}

class UserFromId(Resource):
    @jwt_required
    def get(self, user_id):
        user_details = UserModel.finduser_by_user_id(user_id)
        if user_details:
            return user_details
        return {'message': 'User details not found'}

class UserDetails(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=False,
                        help="This field is optional"
                        )
    parser.add_argument('password',
                        type=str,
                        required=False,
                        help="This field is optional"
                        )
    parser.add_argument('email',
                        type=str,
                        required=False,
                        help="This field is optional"
                        )
    parser.add_argument('role',
                        type=str,
                        required= False,
                        help="This field is optional"
                        )


    @jwt_required
    def get(self, username):
        
        userdetails = UserModel.finduser_by_username(username)
        
        return userdetails
    
    @jwt_required
    def delete(self, username):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message':'Admin Privileges Required'},401

        user = UserModel.find_by_username(username)
        if user:
            del_status = UserModel.delete_user(username)
            if del_status:
                return {'message' : "Unable to delete user '{}'".format(username)}
            return {'message' : 'User deleted Successfully'}

        return {'message' : 'Unable to find User'},404

    @jwt_required
    def put(self, username):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message':'Admin Privileges Required'},401

        data = UserDetails.parser.parse_args()
        update_user = UserModel.update_user(data, username)
        
        if update_user:
            return {'message' : 'User details updated Successfully'}

        return {'message' : 'Unable to update User'},404 
class UserLogin(Resource):
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
    def post(self):
        data = self.parser.parse_args()
        # read from database to find the user and then check the password
        user = UserModel.find_by_username(data['username'])

        if user and check_encrypted_password(data['password'],user.password ):
            # when authenticated, return a fresh access token and a refresh token
            access_token = create_access_token(identity=user.role, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"message": "Invalid Credentials!"}, 401

class UserLogOut(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {'message': 'User has been logged out'}, 200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        
        return {'access_token' : new_token},200
