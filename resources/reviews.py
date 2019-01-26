from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
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
    def put(self):
        #   This method should be used in the case of updating reviews.
        pass

    @jwt_required
    def post(self):
        args = post_parser.parse_args()
        review_args = args
        review = reviews.create_review(review_args)
        return {'review': review}

    @jwt_required
    def delete(self, review_id):
        review = ReviewModel.objects.get(id=id)
        review.delete_review(args)
        return True


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
    @jwt_required
    def get(self, instructor_id):
        review_list = reviews.get_reviews(instructor_id)
        return {'reviews': review_list}
