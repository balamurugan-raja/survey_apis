import mongoengine


data = dict(
    username='balamuruganraja',
    password='Tcs2020',
    host='mongodb://balamuruganraja:Tcs2020@test1-shard-00-00-apxrb.azure.mongodb.net:27017,test1-shard-00-01-apxrb.azure.mongodb.net:27017,test1-shard-00-02-apxrb.azure.mongodb.net:27017',
    ssl=True,
    replicaSet= 'Test1-shard-0',
    authentication_source='admin',
    retryWrites= 'true',
    w='majority'
)

def global_init():
    mongoengine.register_connection(alias='userdb', name='User', **data)
    mongoengine.register_connection(alias='surveydb', name='dsurveys', **data)