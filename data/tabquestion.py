import mongoengine

class TabQuestion(mongoengine.EmbeddedDocument):
    q_id = mongoengine.FloatField()
    q_text = mongoengine.StringField()
    q_responsetype = mongoengine.StringField()
    q_responseoptions = mongoengine.ListField(mongoengine.StringField())