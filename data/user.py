import mongoengine

class User(mongoengine.Document):
    _id = mongoengine.FloatField()
    email = mongoengine.StringField()
    username = mongoengine.StringField()
    password = mongoengine.StringField()

    meta = {
            'db_alias': 'userdb',
            'collection':'userlist'  
    }