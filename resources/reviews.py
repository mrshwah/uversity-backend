from flask_restful import Resource, reqparse
import services.reviews as reviews
from models.reviews import Review as ReviewModel

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


class Review(Resource):
    def get(self, id):
        review = ReviewModel.objects(id__exists=id)[0]
        review = review.to_dict()
        return {'review': review}

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


post_parser_list = reqparse.RequestParser()
args = ['comment',
        'poster_id',
        'instructor_id',
        'class_name',
        'environment_rating',
        'organization_rating',
        'clarity_rating',
        'expertise_rating']
for arg in args:
    post_parser_list.add_argument(arg)


class ReviewList(Resource):
    def get(self):
        reviews = [ob.to_dict() for ob in ReviewModel.objects()]
        return reviews
