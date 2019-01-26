from mongoengine import Document, StringField


class Review(Document):
    comment = ""
    environment_rating = 0
    organization_rating = 0
    clarity_rating = 0
    expertise_rating = 0

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

