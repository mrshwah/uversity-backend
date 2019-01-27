from mongoengine import Document, StringField, ListField, ReferenceField, FloatField


class Instructor(Document):
    reputation = FloatField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: str(v) for (k, v) in dictionary.items()}


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
        try:
            dictionary['instructor'] = Instructor.objects.get(id=dictionary['instructor']).to_dict()
        except KeyError:
            pass
        dictionary['_id'] = str(dictionary['_id'])
        return {k: v for (k, v) in dictionary.items() if k != '_id'}
