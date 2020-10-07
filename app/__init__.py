import re

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_mongoengine import MongoEngine

from app.common import response as resp_serv
from app.data.user import User

db = MongoEngine()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_pyfile('app-config.cfg')


db.init_app(app)


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
        user = User.objects(username=login).first()
    else:
        user = User.objects(email=login).first()
    if user and bcrypt.check_password_hash(user.password, password):
        user.id = str(user.id)
        return user


def identity(payload):
    user_id = payload['identity']
    return User.objects(id=user_id).first()


jwt = JWT(app, authenticate, identity)
# /JWT


if __name__ == '__main__':
    app.run()
