from flask import Flask
from flask_cors import CORS

from main.model import db


def create_app(config="LocalConfig"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("main.config." + config)
    app.logger.debug(app.config.get("SQLALCHEMY_DATABASE_URI"))

    origins = (app.config.get("FRONTEND_ORIGINS")).split(",")
    app.logger.debug(origins)

    cors = CORS(app, origins=origins)

    db.init_app(app)

    from .bluetooth.controller.bluetoothController import bp as bluetooth_blueprint

    #     Blueprints
    app.register_blueprint(bluetooth_blueprint)

    return app
