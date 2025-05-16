from datetime import timedelta


class Config:

    SECRET_KEY = "ohE5yNzyAzuWVhex5ij0Ue40vg8o62g4lhuu7i5-EHc"
    FLASK_APP = "app:create_app_v1"


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:4123@localhost/testbase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # testkey
    SECRET_KEY = "ohE5yNzyAzuWVhex5ij0Ue40vg8o62g4lhuu7i5-EHc"
    API_TITLE = "QuillStore"
    API_VERSION = "v0.7.6"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    DEBUG = True
    JWT_SECRET_KEY = "W4-mPLLUHFNYeyiLSJ_d9yZpD5mUhNqoDHna2xcq3Eg"
    # default expire time
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=5)


class ProdConfig(Config):
    SECRET_KEY = ""  # Use env vars in production
    JWT_SECRET_KEY = ""  # Use env vars in production
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=5)
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
