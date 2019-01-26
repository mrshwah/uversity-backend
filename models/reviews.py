from mongoengine import Document, StringField, IntField


class Review(Document):
    comment = StringField()
    poster_id = StringField(required=True)
    instructor_id = StringField(required=True)
    class_name = StringField(required=True)
    environment_rating = IntField(required=True)
    organization_rating = IntField(required=True)
    clarity_rating = IntField(required=True)
    expertise_rating = IntField(required=True)

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

