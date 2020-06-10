from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from flask_restful import Resource, reqparse
from pprint import pprint
from flask_jwt import jwt_required
from data.template import Template
from data.tabstructure import Tabstructure
from data.tabquestion import TabQuestion
from pprint import pprint
import json

class Templatemodel(Resource):
    
    
    def find_by_templatename(templatename) -> Template:
        pprint(templatename)
        existingtemplateobject = Template.objects(name=templatename).first()
        if existingtemplateobject:
            templateobject = existingtemplateobject.to_json()
            return templateobject
        else:
            return existingtemplateobject
    
      
    def find_by_templateid(templateid) -> Template:
        pprint(templateid)
        templateobject = Template.objects(_id=templateid).first()
                
        if templateobject:
            pprint(templateobject.name)
        else:
            templateobject = None
        return templateobject

   
    
    def find_all_templates()  -> Template:
        template = Template()
        pprint('find all template method reached')
        queryset = Template.objects().order_by('-_id')
        template_collection = queryset.to_json()
        #for temp in queryset:
        #    template_collection.append(temp.to_json)
           #template_collection = Templatemodel.responsemapper(temp)
        
        pprint(template_collection)
        
        return template_collection
   
    
    def requestmapper(data)  -> Template:
        pprint("Entered Mapper method")
        template = Template()
        template.name =data['template_name']

        temp_taglist = []
        for tag in data['tags']:
            temp_taglist.append(tag)
        
        template.tags = temp_taglist
        template.templatecreator_id = data['templatecreator_id']

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

        template.tabs = temp_tablist            
        pprint(template)
                     
            
        return template
    
    def responsemapper(queriedtemplate):
        pprint("Entered Response Mapper method")

        responsetemplate = [{'template_id': queriedtemplate._id, 'template_name':queriedtemplate.name, "tags":[] }]
        
        
        tabquestions= []

        responsetemplate['_id': queriedtemplate._id]
        responsetemplatetags= []
        for tags in queriedtemplate.tags:
            responsetemplatetags.append(tags)
        
        responsetabs = []
        for tabs in queriedtemplate.tabs:
            tab_questions = []
            for question in queriedtemplate.tabs.tabquestions:
                response_options = []
                for response in queriedtemplate.tabs.tabquestions.responseoptions:
                    response_question = [{'q_id': question.q_id, 'q_text': question.q_text, 'responseoptions':[]} ]
            response_tab= [{'tabname': tabs.tabname, 'tab_questions': []}]
            responsetabs.append()
        response


        responsearray = []
        template = Template()
        template.name =data['template_name']

        temp_taglist = []
        for tag in data['tags']:
            temp_taglist.append(tag)
        
        pprint(temp_taglist)
        template.tags = temp_taglist

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

        template.tabs = temp_tablist            
        pprint(template)
                     
            
        return template
    
    
    def getcounter():
        template = Template()
        counter = 1
        firsttemplate = Template.objects().order_by('-_id').first()
        if firsttemplate:
            counter = (firsttemplate._id) + 1
            pprint(counter)
        return counter
    

