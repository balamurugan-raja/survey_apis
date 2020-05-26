import mongoengine
import tabresponses

class surveyresponses(mongoengine.EmbeddedDocument)
    _id = mongoengine.FloatField()
    email = mongoengine.StringField()
    username = mongoengine.StringField()
    password = mongoengine.StringField()

    surveys = mongoengine.EmbeddedDocumentListField(tabresponses)

    meta = {
            'db_alias': 'surveydb',
            'collection':'surveyresponses'
    }