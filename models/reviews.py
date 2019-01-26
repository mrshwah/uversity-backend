from mongoengine import Document, StringField, IntField


class Review(Document):
    comment = StringField()
    poster_id = StringField()
    instructor_id = StringField()
    class_name = StringField()
    environment_rating = IntField()
    organization_rating = IntField()
    clarity_rating = IntField()
    expertise_rating = IntField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

