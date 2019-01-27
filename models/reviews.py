from mongoengine import Document, StringField, IntField, FloatField, ReferenceField
from models.users import User, Instructor


class Review(Document):
    comment = StringField()
    poster = ReferenceField(User)
    instructor = ReferenceField(Instructor)
    class_name = StringField(required=True)
    environment_rating = IntField(required=True)
    organization_rating = IntField(required=True)
    clarity_rating = IntField(required=True)
    expertise_rating = IntField(required=True)
    aggregate_rating = FloatField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['poster'] = User.objects.get(id=dictionary['poster']).to_dict()
        dictionary['instructor'] = User.objects.get(instructor=dictionary['instructor']).to_dict()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

    def calculate_aggregate(self):
        summed = self.clarity_rating + self.environment_rating + self.environment_rating + self.organization_rating
        self.aggregate_rating = summed / 4
