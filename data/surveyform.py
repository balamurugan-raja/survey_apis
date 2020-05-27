import mongoengine
from data.tabstructure import Tabstructure
import datetime

class Surveyform(mongoengine.Document):
    _id = mongoengine.FloatField()
    survey_name = mongoengine.StringField()
    template_id = mongoengine.FloatField()
    surveycreator_id = mongoengine.FloatField()
    surveytags = mongoengine.ListField(mongoengine.StringField())
    survey_creationdate = mongoengine.DateTimeField(default=datetime.datetime.now)    
    tabs = mongoengine.EmbeddedDocumentListField(Tabstructure)
       
    
    meta = {
            'db_alias': 'surveydb',
            'collection':'surveydata',
            'inheritance': True
            }