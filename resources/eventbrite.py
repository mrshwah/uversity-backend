import os
from flask_restful import Resource


class ClientId(Resource):
    def get(self):
        client_id = os.environ.get('EB_CLIENT_ID')
        return {'client_id': client_id}
