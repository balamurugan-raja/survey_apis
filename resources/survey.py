from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps


class Survey(Resource):
    client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
    surveydb = client["dsurveys"]
    survey_col = surveydb["surveydata"]

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank !"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
       pass

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        pass

    @classmethod
    def insert(cls, item):
        pass

    @jwt_required()
    def delete(self, name):
        pass

    @jwt_required()
    def put(self, name):
        pass

    @classmethod
    def update(cls, item):
       pass


class Surveylist(Resource):
    client = pymongo.MongoClient("mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017/test?ssl=true&replicaSet=Test1-shard-0&authSource=admin&retryWrites=true&w=majority")
    surveydb = client["dsurveys"]
    survey_col = surveydb["surveydata"]
    
    def get(self):
        pass
