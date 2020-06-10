from flask import Flask, jsonify, request, render_template, url_for, session, redirect
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
from pprint import pprint
from flask_jwt import JWT, jwt_required
from security import   authenticate, identity

from security import authenticate, identity
from resources.user import UserRegister, UserArray, UserDetails
from resources.survey import Survey, Surveydata, Surveyresponse, GetSurveyResponses
from resources.template import Template, TemplateArray, Templatedata
from models.user import UserModel
import mongoengine
import data.mongo_setup as mongo_setup

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rb'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(UserArray, '/userarray')
api.add_resource(UserDetails, '/user/<string:username>')

api.add_resource(Survey, '/survey')
api.add_resource(Surveydata, '/surveydata/<string:name>')
api.add_resource(Surveyresponse, '/surveyresponse')
api.add_resource(GetSurveyResponses, '/surveyresponses/<int:survey_id>')



api.add_resource(Template, '/template')
api.add_resource(Templatedata, '/templatedata/<string:name>')
api.add_resource(TemplateArray, '/templatearray')

mongo_setup.global_init()

if __name__ == '__main__':
    app.run(debug=True)  
