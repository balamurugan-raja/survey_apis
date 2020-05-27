import mongoengine
from data.tabquestion import TabQuestion

class Tabstructure(mongoengine.EmbeddedDocument):
    tabname = mongoengine.StringField()
    tabquestions = mongoengine.EmbeddedDocumentListField(TabQuestion)