from mongoengine import Document, ReferenceField, FloatField, ListField

class Instructor(Document):
    user = ReferenceField('User')
    reputation = FloatField()
    history = ListField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}


