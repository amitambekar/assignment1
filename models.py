from mongoengine import *


class Tenant(Document):
    columns = ListField(StringField(max_length=50))


class ProjectMetadata(Document):
    tenant_id = ReferenceField(Tenant)
    file_location = StringField(required=True, max_length=200)
    s3_uploaded_model_location = StringField(required=True, max_length=200)
    model_evalution_result = IntField(required=True, max_length=50)