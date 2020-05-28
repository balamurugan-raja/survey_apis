from flask import Flask, jsonify
from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from models.survey import Surveymodel
from pprint import pprint

class Survey(Resource):
    #parser = reqparse.RequestParser()
    #data = request.get_json()

    #@jwt_required()
    def post(self):
        data = request.get_json()
        
        #data = Survey.parser.parse_args()
        pprint('survey post method')
        surveyindb = Surveymodel.find_by_surveyname(data['survey_name'])
        if surveyindb:
            return {"message": "Survey with that Name already exists."}, 400
        
        

        survey_tobecreated = Surveymodel.requestmapper(data)
        
        survey = survey_tobecreated.save()
        
        if survey_tobecreated:
            pprint(survey_tobecreated._id)
            return {"message": "Survey created successfully.", "survey_id": survey_tobecreated._id}, 201
        else:
            return {"message": "Survey Not Created."}
    
    #@jwt_required()
    def get(self):
        
        pprint("reached survey array method")
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


class Surveydata(Resource):
    #@jwt_required()
    def get(self,name):
        surveyindb = Surveymodel.find_by_surveyname(name)
        if surveyindb:
            return surveyindb
        else:
            return {"message": "No such Survey exists."}

class SurveyArray(Resource):
    #@jwt_required()
    def get(self):
        surveysindb = Surveymodel.find_all_surveys()
        if surveysindb:
            return surveysindb
        else:
            return {"message": "No Surveys found."}

class Surveyresponse(Resource):

    def post(self):
        pprint('surveyresponse post method')
        data = request.get_json()
        surveres_tobecreated = Surveymodel.surveyresmapper(data)
        surveyres = surveres_tobecreated.save()
        
        if surveyres:
            pprint(surveyres._id)
            return {"message": "Survey Response Submitted successfully."}, 201
        else:
            return {"message": "Survey Response Not Submitted."}

