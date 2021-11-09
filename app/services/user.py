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


@jwt_required()
def change_password(req):
    current_password = req.json['current_password']
    new_password = req.json['new_password']
    confirm_new_password = req.json['confirm_new_password']
    current_hashed_password = current_identity.password
    if bcrypt.check_password_hash(current_hashed_password, current_password) is False:
        return resp_comm.response(
            message='Incorrect password',
            data={
                'user': user_repo.to_dto(current_identity)
            },
            success=False
        ), 400
    if new_password != confirm_new_password:
        return resp_comm.response(
            message='Password confirmation not matched',
            data={},
            success=False
        ), 400
    changed_password = user_repo.change_password(current_identity.id, bcrypt.generate_password_hash(new_password).decode('utf-8'))
    return resp_comm.response(
        message='Password updated',
        data=user_repo.to_dto(changed_password)
    ), 200
