from mongoengine import Document, StringField


class User(Document):
    eb_id = StringField()
    oauth_token = StringField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}
