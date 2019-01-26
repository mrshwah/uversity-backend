from mongoengine import *
from models.users import User


class Course(Document):
    eb_id = StringField(required=True)
    instructor_id = StringField(required=True)
    name = StringField(required=True)
    # location = GeoPointField(required=True)
    category = StringField()
    # difficulty = IntField()
    start = DateTimeField()
    end = DateTimeField()
    student_list = ListField(ReferenceField(User))
    capacity = IntField()

    def to_dict(self):
        dictionary = self.to_mongo()
        dictionary['student_list'] = [student.to_dict() for student in dictionary['student_list']]
        dictionary = {k: v for (k, v) in dictionary.items() if k != '_id'}
        dictionary['start'] = dictionary['start'].isoformat(' ')
        dictionary['end'] = dictionary['end'].isoformat(' ')
        return dictionary

    def enroll_user(self, user_id):
        user = User.objects.get(eb_id=user_id)
        try:
            user_course_history = CourseHistory.objects(user=user_id)
        except IndexError:
            user_course_history = CourseHistory(user=user)
        user_course_history.courses += [self]
        self.student_list += [user_id]
        self.capacity -= 1
        self.save()


class CourseHistory(Document):
    user = ReferenceField(User)
    courses = ListField(ReferenceField(Course))
