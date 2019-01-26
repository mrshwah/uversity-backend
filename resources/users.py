from flask_restful import Resource, reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('access_code')


class User(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
