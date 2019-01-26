from flask import Flask
from flask_cors import CORS
import resources
import models
import services
import config


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config.Config)
    resources.init_app(app)
    models.init_app(app)
    services.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
