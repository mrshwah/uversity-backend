from mongoengine import Document, StringField, URLField


class Category(Document):
    name = StringField(required=True)
    image = URLField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items()}
