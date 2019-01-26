from mongoengine import Document, StringField


class User(Document):
    eb_id = StringField()
