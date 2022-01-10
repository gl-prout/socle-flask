import re

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_mongoengine import MongoEngine
from flask_swagger_ui import get_swaggerui_blueprint

from app.common import response as resp_serv
from app.data.user import User
from app.repository import user as user_repo

# Configurations
db = MongoEngine()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_pyfile('app-config.cfg')
# /Configurations

# Database
db.init_app(app)
# /Database


# Error handling
@app.errorhandler(400)
def bad_request(e):
    return handle_error(e)


@app.errorhandler(401)
def unauthorized_access(e):
    return handle_error(e)


@app.errorhandler(404)
def not_found(e):
    return handle_error(e)


@app.errorhandler(405)
def not_allowed(e):
    return handle_error(e)


@app.errorhandler(500)
def internal_error(e):
    return handle_error(e)


def handle_error(e):
    return resp_serv.response(
        success=False,
        message=e.name,
        data={
            'description': e.description
        }
    ), e.code
# /Error handling


# JWT
def authenticate(login, password):
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s.]+$", login):
        user = user_repo.find_by_username(login)
    else:
        user = user_repo.find_by_email(login)
    if user and bcrypt.check_password_hash(user.password, password):
        user.id = str(user.id)
        return user


def identity(payload):
    user_id = payload['identity']
    return User.objects(id=user_id).first()


jwt = JWT(app, authenticate, identity)
# /JWT


# Swagger
SWAGGER_URL = '/api/docs'
API_URL = app.config['BASE_URL'] + 'apidoc/api.yml'
# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Socle flask"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)
app.register_blueprint(swaggerui_blueprint)
# /Swagger


if __name__ == '__main__':
    app.run()
