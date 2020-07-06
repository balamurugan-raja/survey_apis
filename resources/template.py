from flask import Flask, jsonify
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from models.template import Templatemodel
from pprint import pprint

class Template(Resource):
    #parser = reqparse.RequestParser()
    #data = request.get_json()
    @jwt_required
    def post(self):
        data = request.get_json()
        
        #data = Template.parser.parse_args()
        pprint('template post method')
        templateindb = Templatemodel.find_by_templatename(data['template_name'])
        if templateindb:
            return {"message": "Template with that Name already exists."}, 400
        
        

        template_tobecreated = Templatemodel.requestmapper(data)
        template_tobecreated._id = Templatemodel.getcounter()
        saved_template = template_tobecreated.save()
        
        if saved_template:
            pprint(saved_template._id)
            return {"message": "Template created successfully.", "template_id": saved_template._id}, 201
        else:
            return {"message": "Template Not Created."}
    
    @jwt_required
    def get(self):
        
        pprint("reached template array method")
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
    
    @jwt_required
    def put(self):
        data = request.get_json()
        
        #data = Template.parser.parse_args()
        pprint('template post method')
        templateindb = Templatemodel.find_by_templatename(data['template_name'])
        if templateindb is None:
            return {"message": "Template with that Name doesn't exist."}, 400
        
        

        template_tobeupdated = Templatemodel.requestmapper(data)
        template_tobeupdated._id = data['template_id']
        saved_template = template_tobeupdated.save()
        
        if saved_template:
            pprint(saved_template._id)
            return {"message": "Template Updated successfully.", "template_id": saved_template._id}, 201
        else:
            return {"message": "Template Not Saved."}


class Templatedata(Resource):
    @jwt_required
    def get(self,name):
        templateindb = Templatemodel.find_by_templatename(name)
        if templateindb:
            return templateindb
        else:
            return {"message": "No such Template exists."}

class TemplateArray(Resource):
    @jwt_required
    def get(self):
        templatesindb = Templatemodel.find_all_templates()
        if templatesindb:
            return templatesindb
        else:
            return {"message": "No Templates found."}

