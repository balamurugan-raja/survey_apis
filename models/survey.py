from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required
from data.surveyform import Surveyform
from data.surveyresponse import Surveyresponse
from data.surveyscore import Surveyscore
from data.tabstructure import Tabstructure
from data.tabquestion import TabQuestion
from data.tabresponse import Tabresponse, Qresponses
from models.user import UserModel
from pprint import pprint
import json

class Surveymodel(Resource):
    
    
    def find_by_surveyname(surveyname) -> Surveyform:
        
        surveyobject = Surveyform.objects(survey_name=surveyname).first()
        if surveyobject:
            retsurveyobject = surveyobject.to_json()
            return retsurveyobject
        return surveyobject
    
      
    def find_by_surveyid(surveyid) -> Surveyform:
        
        surveyobject = Surveyform.objects(_id=surveyid).first()
                
        if surveyobject:
            pprint(surveyobject.name)
        else:
            surveyobject = None
        return surveyobject

   
    
    def find_all_surveys()  -> Surveyform:
        survey = Surveyform()
        queryset = Surveyform.objects().order_by('-_id')
        survey_collection = queryset.to_json()
                
        return survey_collection

    def find_all_surveys_for_userid(creator_id)  -> Surveyform:
        
        
        survey = Surveyform()
        queryset = Surveyform.objects(surveycreator_id=creator_id).order_by('-_id')
        
        survey_collection = []
        for survey_obj in queryset:
            
            taglist = []
            for tag in survey_obj['surveytags'] :
                taglist.append(tag)
            user = UserModel.finduser_by_user_id(survey_obj.surveycreator_id)
            if user:
               s_creator_name = user.username
            else:
                s_creator_name = "Anonymous"

            survey_object = {'survey_id': survey_obj._id, 'survey_name':survey_obj.survey_name, 'surveycreator_id': survey_obj.surveycreator_id, 's_creator_name': s_creator_name, 'surveytags' : taglist}
            survey_collection.append(survey_object)

        return survey_collection
   
    
    def requestmapper(data)  -> Surveyform:
        
        survey = Surveyform()
        survey._id = Surveymodel.getcounter()
        survey.survey_name =data['survey_name']
        survey.template_id = data['template_id']
        survey.surveycreator_id = data['surveycreator_id']
        
        temp_taglist = []
        for tag in data['surveytags']:
            temp_taglist.append(tag)
        
        survey.surveytags = temp_taglist

        temp_tablist = []
        for tab in data['tabs']:
            tabobject = Tabstructure()
            tabobject.tabname = tab['tabname']
            tabquestionobjectlist = []
            for tabitem in tab['tabquestions']:
                tabquestionobject= TabQuestion()
                tabquestionobject.q_id = tabitem['q_id']
                tabquestionobject.q_text = tabitem['q_text']
                tabquestionobject.q_responsetype = tabitem['q_responsetype']
                if tabquestionobject.q_responsetype == "select" :
                    responseoptions =[]
                    for resoption in tabitem['q_responseoptions']:
                        responseoptions.append(resoption)
                    tabquestionobject.q_responseoptions= responseoptions
                tabquestionobjectlist.append(tabquestionobject)
            tabobject.tabquestions = tabquestionobjectlist
            temp_tablist.append(tabobject)

        survey.tabs = temp_tablist            
        return survey
    
    def get_sur_res_by_surveyid(survey_id) -> Surveyresponse:
        surveyresobject = Surveyresponse.objects(survey_id=survey_id)
        if surveyresobject:
            retsurveyresobject = surveyresobject.to_json()
            return retsurveyresobject
        else:
            return surveyresobject
    
    def get_sur_res_by_part_id(survey_id, participant_id) -> Surveyresponse:
        surveyresobject = Surveyresponse.objects(survey_id=survey_id, participant_id=participant_id)
        if surveyresobject:
            retsurveyresobject = surveyresobject.to_json()
            return retsurveyresobject
        else:
            return surveyresobject
    
    
    def surveyresmapper(data) -> Surveyresponse:
        survey = Surveyresponse()
        survey._id = Surveymodel.getrespcounter()
        survey.participant_id = data['participant_id']
        survey.survey_id = data['survey_id']      
        temp_tablist = []
        for tab in data['tab_responses']:
            tabobject = Tabresponse()
            tabobject.tabname = tab['tabname']
            tabobject.tab_score = tab['tab_score']
            tabquestionobjectlist = []
            for tabitem in tab['q_responses']:
                tabquestionobject= Qresponses()
                tabquestionobject.q_id = tabitem['q_id']
                resp_text = tabitem['resp_text']
                if resp_text:
                    tabquestionobject.resp_text = tabitem['resp_text']
                    pprint(tabitem['resp_text'])
                
                resp_num = tabitem['resp_num']
                if resp_num:
                    tabquestionobject.resp_num = tabitem['resp_num']
                tabquestionobject.resp_score = tabitem['resp_score']
                tabquestionobjectlist.append(tabquestionobject)
            tabobject.q_responses = tabquestionobjectlist
            temp_tablist.append(tabobject)

        survey.tab_responses = temp_tablist 

        temp_survey_scores = []
        for temp_list in data['survey_scores']:
            temp_surveyscore = Surveyscore()
            temp_surveyscore.tab_name = temp_list['tab_name']
            temp_surveyscore.tab_score = temp_list['tab_score']
            temp_survey_scores.append(temp_surveyscore)
        
        survey.survey_scores = temp_survey_scores
        
        return survey
    
    def getcounter():
        survey = Surveyform()
        counter = 1
        firstsurvey = Surveyform.objects().order_by('-_id').first()
        if firstsurvey:
            counter = (firstsurvey._id) + 1
        return counter
    
    def getrespcounter():
        survey = Surveyresponse()
        counter = 1
        firstsurvey = Surveyresponse.objects().order_by('-_id').first()
        if firstsurvey:
            counter = (firstsurvey._id) + 1
            
        return counter
    

