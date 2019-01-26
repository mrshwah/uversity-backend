from mongoengine import *


class Course(Document):
    eb_id = StringField(required=True)
    teacher = ReferenceField('Teacher')
    title = StringField()
    location = GeoPointField(required=True)
    category = ReferenceField('Category')
    difficulty = IntField()
    image_links = ListField(URLField())
    start_date_and_time = ComplexDateTimeField()
    end_date_and_time = ComplexDateTimeField()
    student_list = ListField()
    capacity = IntField()

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}
