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

class Templatemodel(Resource):
    
    
    def find_by_templatename(templatename) -> Template:
        pprint(templatename)
        templateobject = Template.objects(name=templatename).first()
                
        if templateobject:
            pprint(templateobject.name)
        else:
            templateobject = None
        return templateobject
    
      
    def find_by_templateid(templateid) -> Template:
        pprint(templateid)
        templateobject = Template.objects(_id=templateid).first()
                
        if templateobject:
            pprint(templateobject.name)
        else:
            templateobject = None
        return templateobject

   
    
    def create_template(teamplatetobesaved)  -> Template:
        template = Template()
        template._id =data['_id']
        template.name =data['template']

        template.save()
        return template
   
    
    def requestmapper(data)  -> Template:
        pprint("Entered Mapper method")
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

