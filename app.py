from flask import Flask, jsonify, request, render_template, url_for, session, redirect
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
from pprint import pprint
from flask_jwt import JWT, jwt_required
from security import   authenticate, identity

from security import authenticate, identity
from resources.user import UserRegister, UserArray
from resources.survey import Survey 
from resources.template import Template 
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
api.add_resource(Survey, '/survey/<string:surveyname>')
api.add_resource(Template, '/template')

mongo_setup.global_init()

if __name__ == '__main__':
    app.run(debug=True)  
