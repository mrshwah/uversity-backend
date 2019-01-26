from mongoengine import Document, StringField, ListField, ReferenceField, FloatField


class Instructor(Document):
    reputation = FloatField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}


class User(Document):
    eb_id = StringField(unique=True, required=True)
    oauth_token = StringField()
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    # profile_img = ImageField()
    interests = ListField(required=False)
    instructor = ReferenceField(Instructor)

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['instructor'] = dictionary['instructor'].to_dict()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

