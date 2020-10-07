from app.common import response as resp_comm
from app.constants import name
from app.repository import user as user_repo
from flask import abort
from flask_bcrypt import Bcrypt
from flask_jwt import current_identity, jwt_required

bcrypt = Bcrypt(name)


def create_user(req):
    email = req.json['email']
    username = req.json['username']
    uexist = user_repo.find_by_email(email)
    upseudo = user_repo.find_by_username(username)
    if uexist:
        abort(400, description='Email already in use')
    if upseudo:
        abort(400, description='Username already in use')
    plain_password = req.json['password']
    password = bcrypt.generate_password_hash(plain_password)
    user = user_repo.create(email, username, password)
    userdata = user_repo.to_dto(user)
    return resp_comm.response(
        message='New user subscribed',
        data={
            'user': userdata,
        }
    ), 201


@jwt_required()
def my_profile():
    me = user_repo.to_dto(current_identity)
    return resp_comm.response(
        message='Profile retrieved',
        data={
            'user': me,
        }
    ), 200
