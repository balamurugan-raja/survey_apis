import mongoengine

class Surveyscore(mongoengine.EmbeddedDocument):
    tab_name = mongoengine.StringField()
    tab_score = mongoengine.FloatField()
    