from flask import Flask
from .extensions import db, smorest_api, migrater, jwt_manager, bcrypter
from config import DevConfig
from .api.Users import account_blp
from .api.Quills import quill_blp
from .api.Common import common_blp
from .api.Auth import auth_blp
from dotenv import load_dotenv

load_dotenv()


def create_app_v1():

    App = Flask(__name__)

    App.config.from_object(DevConfig)

    db.init_app(App)

    smorest_api.init_app(App)

    smorest_api.register_blueprint(account_blp)
    smorest_api.register_blueprint(quill_blp)
    smorest_api.register_blueprint(common_blp)
    smorest_api.register_blueprint(auth_blp)

    bcrypter.init_app(App)

    jwt_manager.init_app(App)

    migrater.init_app(App, db)

    return App
