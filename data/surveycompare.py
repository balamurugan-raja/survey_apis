import mongoengine



class ref_tabscores(mongoengine.EmbeddedDocument):
    tab_name = mongoengine.StringField()
    tab_score = mongoengine.FloatField()
    
    
class ref_surveyscores(mongoengine.EmbeddedDocument):
    ref_surveyname = mongoengine.StringField()
    ref_tabscorelist = mongoengine.EmbeddedDocumentListField(ref_tabscores)


class Surveycompare(mongoengine.Document):
    _id = mongoengine.FloatField()
    survey_id = mongoengine.FloatField()
    ref_surveyscorelist = mongoengine.EmbeddedDocumentListField(ref_surveyscores)
    
    meta = {
            'db_alias': 'surveydb',
            'collection':'surveycompare',
            'inheritance': True
            }