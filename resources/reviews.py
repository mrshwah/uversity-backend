from flask_restful import Resource, reqparse
import services.reviews as reviews
from models.reviews import Review as ReviewModel

post_parser = reqparse.RequestParser()

review_args = ['comment',
        'poster_id',
        'instructor_id',
        'class_name',
        'environment_rating',
        'organization_rating',
        'clarity_rating',
        'expertise_rating']
for arg in review_args:
    post_parser.add_argument(arg)


class Review(Resource):
    def get(self, resource_id):
        review = ReviewModel.objects(id__exists=resource_id)[0]
        review = review.to_dict()
        return {'review': review}

    def put(self, review_args):
        args = post_parser.parse_args()
        review_args = args
        review = reviews.update_review(review_args)
        review.save()
        pass

    def post(self):
        args = post_parser.parse_args()
        review_args = args
        review = reviews.create_review(review_args)
        return {'review': review}

    def delete(self, id):
        reviews = ReviewModel.objects.get(id)
        reviews.delete_review(review_args)
        return True


# post_parser_list = reqparse.RequestParser()
# args = ['comment',
#         'poster_id',
#         'instructor_id',
#         'class_name',
#         'environment_rating',
#         'organization_rating',
#         'clarity_rating',
#         'expertise_rating']
# for arg in args:
#     post_parser_list.add_argument(arg)


class ReviewList(Resource):
    def get(self):
        reviews = [ob.to_dict() for ob in ReviewModel.objects()]
        return reviews
