from mongoengine import *


class Course(Document):
    eb_id = StringField(required=True)
    # instructor = ReferenceField('Instructor')
    name = StringField(required=True)
    # location = GeoPointField(required=True)
    category = StringField()
    # difficulty = IntField()
    # image_links = ListField(URLField())
    start = DateTimeField()
    end = DateTimeField()
    # student_list = ListField()
    capacity = IntField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary = {k: v for (k, v) in dictionary.items() if k != '_id'}
        dictionary['start'] = dictionary['start'].isoformat(' ')
        dictionary['end'] = dictionary['end'].isoformat(' ')
        return dictionary
