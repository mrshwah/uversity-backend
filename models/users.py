from mongoengine import Document, EmbeddedDocument, StringField, ImageField, ListField, ReferenceField, FloatField, EmbeddedDocumentField


class Instructor(EmbeddedDocument):
    # user = ReferenceField(User)
    reputation = FloatField()
    history = ListField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['user'] = User.objects.get(id=dictionary['user']).to_dict()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}


class User(Document):
    eb_id = StringField(unique=True, required= True)
    oauth_token = StringField()
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    # profile_img = ImageField()
    interests = ListField(required=False)
    instructor = EmbeddedDocumentField(Instructor)

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}




