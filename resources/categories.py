from flask_restful import Resource
from flask_jwt_extended import jwt_required
import services.categories as categories


class CategoryList(Resource):
    @jwt_required
    def get(self):
        category_list = categories.get_categories()
        return {'categories': category_list}
