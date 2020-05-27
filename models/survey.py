from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required
from data.surveyform import Surveyform
from data.tabstructure import Tabstructure
from data.tabquestion import TabQuestion
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
        #for temp in queryset:
        #    survey_collection.append(temp.to_json)
           #survey_collection = Surveymodel.responsemapper(temp)
        
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
    
    def responsemapper(queriedsurvey):
        pprint("Entered Response Mapper method")

        responsesurvey = [{'survey_id': queriedsurvey._id, 'survey_name':queriedsurvey.name, "tags":[] }]
        
        
        tabquestions= []

        responsesurvey['_id': queriedsurvey._id]
        responsesurveytags= []
        for tags in queriedsurvey.tags:
            responsesurveytags.append(tags)
        
        responsetabs = []
        for tabs in queriedsurvey.tabs:
            tab_questions = []
            for question in queriedsurvey.tabs.tabquestions:
                response_options = []
                for response in queriedsurvey.tabs.tabquestions.responseoptions:
                    response_question = [{'q_id': question.q_id, 'q_text': question.q_text, 'responseoptions':[]} ]
            response_tab= [{'tabname': tabs.tabname, 'tab_questions': []}]
            responsetabs.append()
        response


        responsearray = []
        survey = Surveyform()
        survey.name =data['survey_name']

        temp_taglist = []
        for tag in data['tags']:
            temp_taglist.append(tag)
        
        pprint(temp_taglist)
        survey.tags = temp_taglist

        temp_tablist = []
        for tab in data['tabs']:
            tabobject = Tabstructure()
            tabobject.tabname = tab['tabname']
            tabquestionobjectlist = []
            for tabitem in tab['tabquestions']:
                tabquestionobject= TabQuestion()
                tabquestionobject.q_id = tabitem['q_id']
                tabquestionobject.q_text = tabitem['q_text']
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
    
    
    def getcounter():
        survey = Surveyform()
        counter = 1
        firstsurvey = Surveyform.objects().order_by('-_id').first()
        if firstsurvey:
            counter = (firstsurvey._id) + 1
            pprint(counter)
        return counter
    

