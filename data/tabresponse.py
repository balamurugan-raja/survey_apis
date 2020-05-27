import mongoengine

class Tabresponse(mongoengine.EmbeddedDocument):
    tab_name = mongoengine.StringField()
    q_responses = mongoengine.ListField(mongoengine.FloatField())
    score = mongoengine.FloatField()

