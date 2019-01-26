from mongoengine import Document, ReferenceField, FloatField, ListField
from models.users import User


class Instructor(Document):
    user = ReferenceField(User)
    reputation = FloatField()
    history = ListField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['user'] = User.objects.get(id=dictionary['user']).to_dict()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}


