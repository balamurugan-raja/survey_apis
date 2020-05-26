import mongoengine

class tabresponses(mongoengine.EmbeddedDocument)
    survey_id = mongoengine.ObjectIdField()
    q_id = mongoengine.FloatField()
    response =  mongoengine.StringField()
    resp_type = mongoengine.StringField()
    score = mongoengine.ObjectIdField()