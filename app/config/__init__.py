from flask import Flask

from config import config

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(config[env_name])
    
    from app.controller.errors_controller import errors_blueprint
    app.register_blueprint(errors_blueprint)

    from app.controller.benefits_controller import benefits_blueprint
    app.register_blueprint(benefits_blueprint)

    return app
