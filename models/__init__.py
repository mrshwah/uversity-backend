from mongoengine import connect


def init_app(app):
    connect(db=app.config['MONGODB_DB'], username=app.config['MONGODB_USERNAME'],
            password=app.config['MONGODB_PASSWORD'], port=app.config['MONGODB_PORT'], host=app.config['MONGODB_HOST'])
