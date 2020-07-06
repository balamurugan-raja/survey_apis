from flask import Flask, jsonify, request, render_template, url_for, session, redirect
from flask_restful import Resource, Api
from flask_cors import CORS

from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

from pprint import pprint

import mongoengine

from resources.user import UserRegister, UserArray, UserDetails, UserLogin, TokenRefresh, UserLogOut, UserFromId
from resources.survey import Survey, Surveydata, Surveyresponse, GetSurveyResponses, SurveyArray, SurveyfromID
from resources.template import Template, TemplateArray, Templatedata

from models.user import UserModel

import data.mongo_setup as mongo_setup

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 600
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'rb'
CORS(app)
api = Api(app)


jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_loader(identity):
    if identity == "admin":
        return{'is_admin': True}
    return {'is_admin': False}
#jwt = JWT(app, authenticate, identity)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description':'The Authentication Token Has expired',
        'error' : 'token_expired'
    }),401

@jwt.revoked_token_loader
def revoke_token_callback():
    return jsonify({
        'description':'The User has Signed out',
        'error' : 'signed_out'
    }),401
api.add_resource(UserLogin, '/auth')
api.add_resource(UserRegister, '/register')
api.add_resource(UserArray, '/userarray')
api.add_resource(UserDetails, '/user/<string:username>')
api.add_resource(UserFromId, '/userfromid/<int:user_id>')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogOut, '/logout')


api.add_resource(Survey, '/survey')
api.add_resource(Surveydata, '/surveydata/<string:name>')
api.add_resource(Surveyresponse, '/surveyresponse')
api.add_resource(GetSurveyResponses, '/surveyresponses/<int:survey_id>')
api.add_resource(SurveyArray, '/surveyarray/<int:creator_id>')
api.add_resource(SurveyfromID, '/surveyfromid/<int:survey_id>')

api.add_resource(Template, '/template')
api.add_resource(Templatedata, '/templatedata/<string:name>')
api.add_resource(TemplateArray, '/templatearray')

mongo_setup.global_init()

if __name__ == '__main__':
    app.run(debug=True)  
