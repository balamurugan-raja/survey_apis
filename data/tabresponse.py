import mongoengine


class Qresponses(mongoengine.EmbeddedDocument):
    q_id = mongoengine.FloatField()
    resp_text = mongoengine.StringField()
    resp_num = mongoengine.FloatField()
    resp_score = mongoengine.FloatField()
class Tabresponse(mongoengine.EmbeddedDocument):
    tabname = mongoengine.StringField()
    q_responses = mongoengine.EmbeddedDocumentListField(Qresponses)
    tab_score = mongoengine.FloatField()




