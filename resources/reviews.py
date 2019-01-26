from flask_restful import Resource, reqparse
from models.reviews import Review as ReviewModel
import services.reviews as reviews

post_parser = reqparse.RequestParser()
args = ['comment',
        'poster_id',
        'instructor_id',
        'class_name',
        'environment_rating',
        'organization_rating',
        'clarity_rating',
        'expertise_rating']
for arg in args:
    post_parser.add_argument(arg)


class Reviews(Resource):
    def get(self):
        reviews = [ob.to_dict() for ob in ReviewModel.objects()]
        return reviews

    def put(self):
        #   This method should be used in the case of updating reviews.
        pass

    def post(self):
        args = post_parser.parse_args()
        review_args = args
        review = reviews.create_review(review_args)
        return {'review': review}

    def delete(self):
        args = post_parser.parse_args()
        reviews.delete_review(args)
        pass
