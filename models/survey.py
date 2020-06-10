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
from pprint import pprint
import json

class Surveymodel(Resource):
    
    
    def find_by_surveyname(surveyname) -> Surveyform:
        pprint(surveyname)
        surveyobject = Surveyform.objects(survey_name=surveyname).first()
        if surveyobject:
            retsurveyobject = surveyobject.to_json()
            return retsurveyobject
        return surveyobject
    
      
    def find_by_surveyid(surveyid) -> Surveyform:
        pprint(surveyid)
        surveyobject = Surveyform.objects(_id=surveyid).first()
                
        if surveyobject:
            pprint(surveyobject.name)
        else:
            surveyobject = None
        return surveyobject

   
    
    def find_all_surveys()  -> Surveyform:
        survey = Surveyform()
        pprint('find all survey method reached')
        queryset = Surveyform.objects().order_by('-_id')
        survey_collection = queryset.to_json()
                
        pprint(survey_collection)
        
        return survey_collection
   
    
    def requestmapper(data)  -> Surveyform:
        pprint("Entered Mapper method")
        survey = Surveyform()
        survey._id = Surveymodel.getcounter()
        survey.survey_name =data['survey_name']
        survey.template_id = data['template_id']
        survey.surveycreator_id = data['surveycreator_id']
        
        temp_taglist = []
        for tag in data['surveytags']:
            temp_taglist.append(tag)
        
        pprint(temp_taglist)
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
        pprint(survey)
                     
            
        return survey
    
    
    
    
    def surveyresmapper(data) -> Surveyresponse:
        pprint("Entered Mapper method")
        survey = Surveyresponse()
        survey._id = Surveymodel.getrespcounter()
        survey.participant_id = data['participant_id']
                
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

        pprint(survey)
                
        return survey
    
    def getcounter():
        survey = Surveyform()
        counter = 1
        firstsurvey = Surveyform.objects().order_by('-_id').first()
        if firstsurvey:
            counter = (firstsurvey._id) + 1
            pprint(counter)
        return counter
    
    def getrespcounter():
        survey = Surveyresponse()
        counter = 1
        firstsurvey = Surveyresponse.objects().order_by('-_id').first()
        if firstsurvey:
            counter = (firstsurvey._id) + 1
            pprint(counter)
        return counter
    

