import mongoengine
from data.tabstructure import Tabstructure
import datetime

class Template(mongoengine.Document):
    _id = mongoengine.FloatField()
    name = mongoengine.StringField()
    tags = mongoengine.ListField(mongoengine.StringField())
    tabs = mongoengine.EmbeddedDocumentListField(Tabstructure)
    temp_creationdate = mongoengine.DateTimeField(default=datetime.datetime.now)    
    
    meta = {
            'db_alias': 'surveydb',
            'collection':'templates',
            'allow_inheritance': True,
            'index_cls': False   
    }