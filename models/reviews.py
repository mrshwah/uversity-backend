from mongoengine import Document, StringField, IntField, FloatField, ReferenceField
from models.users import User


class Review(Document):
    comment = StringField()
    poster_id = ReferenceField(User)
    instructor_id = StringField(required=True)
    class_name = StringField(required=True)
    environment_rating = IntField(required=True)
    organization_rating = IntField(required=True)
    clarity_rating = IntField(required=True)
    expertise_rating = IntField(required=True)
    aggregate_rating = FloatField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['poster_id'] = User.objects.get(id=dictionary['poster_id']).to_dict()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

