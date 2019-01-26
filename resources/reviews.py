from flask_restful import Resource
from models.reviews import Review as ReviewModel


class Reviews(Resource):
    def get(self):
        reviews = [ob.to_dict() for ob in ReviewModel.objects()]
        return reviews

    def put(self):
        pass

    def delete(self):
        pass
