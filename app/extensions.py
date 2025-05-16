from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrater = Migrate()
smorest_api = Api()
jwt_manager = JWTManager()
bcrypter = Bcrypt()
