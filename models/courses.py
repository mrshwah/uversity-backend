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
    student_list = ListField(StringField())
    capacity = IntField()
    is_cancelled = BooleanField(default=False)

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary = {k: v for (k, v) in dictionary.items() if k != '_id'}
        dictionary['start'] = dictionary['start'].isoformat(' ')
        dictionary['end'] = dictionary['end'].isoformat(' ')
        return dictionary

    def enroll_user(self, user_id):
        self.student_list = self.student_list + [user_id]
        self.capacity -= 1
        self.save()
