import mongoengine
from data.tabresponse import Tabresponse
from data.surveyscore import Surveyscore
import datetime

class Surveyresponse(mongoengine.Document):
    _id = mongoengine.FloatField()
    survey_id = mongoengine.FloatField()
    participant_id = mongoengine.FloatField()
    survey_responsedate = mongoengine.DateTimeField(default=datetime.datetime.now)    
    tab_responses = mongoengine.EmbeddedDocumentListField(Tabresponse)
    survey_scores = mongoengine.EmbeddedDocumentListField(Surveyscore)
    
    
    meta = {
            'db_alias': 'surveydb',
            'collection':'surveyresponses',
            
            }