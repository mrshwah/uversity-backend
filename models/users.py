from mongoengine import Document, StringField, ImageField, ListField, ReferenceField
from models.courses import Course


class User(Document):
    eb_id = StringField(unique=True, required=True)
    oauth_token = StringField()
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    # profile_img = ImageField()
    interests = ListField(required=False)
    course_history = ListField(ReferenceField(Course))

    def to_dict(self):
        dictionary = self.to_mongo()
        return {k: v for (k, v) in dictionary.items() if k != '_id'}

    def add_course(self, course_id):
        course = Course.objects(eb_id=course_id)
        self.course_history += course
        self.save()