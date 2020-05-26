import mongoengine
from data.tabquestion import Tabquestion

class Tabstructure(mongoengine.EmbeddedDocument)
    tabname = mongoengine.StringField()
    tabquestions = mongoengine.EmbeddedDocumentListField(Tabquestion)