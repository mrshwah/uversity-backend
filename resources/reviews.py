from flask_restful import Resource, reqparse
from models.reviews import Review as ReviewModel
import services.reviews as reviews

post_parser = reqparse.RequestParser()
post_parser.add_argument('comment')
post_parser.add_argument('environment_rating')
post_parser.add_argument('organization_rating')
post_parser.add_argument('clarity_rating')
post_parser.add_argument('expertise_rating')


class Reviews(Resource):
    def get(self):
        reviews = [ob.to_dict() for ob in ReviewModel.objects()]
        return reviews

    def put(self):
        pass

    def post(self):
        args = post_parser.parse_args()
        review_args = args
        review = reviews.create_review(review_args)
        return {'review': review}

    def delete(self):
        pass
