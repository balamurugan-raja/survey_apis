from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from models.template import Templatemodel
from pprint import pprint

class Template(Resource):
    #parser = reqparse.RequestParser()
    #data = request.get_json()

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