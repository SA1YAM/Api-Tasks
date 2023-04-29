import os
from flask import Flask
from application.config import LocalDevelopmentConfig
from application.data.models import db
from application.controller.api import api
from flask_cors import CORS
#from flask_caching import Cache
#from flask_mail import Mail

app = None
redis_cache = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    CORS(app)

    app.app_context().push()
    return app


app = create_app()



if __name__ == '__main__':
  # Run the Flask app
  app.run()
