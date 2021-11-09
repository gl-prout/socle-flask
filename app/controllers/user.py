from app.controllers import Controllers as ctrl
from app.services import user as user_serv
from flask import abort, request


def create_user():
    if request.method == 'POST':
        return user_serv.create_user(request)
    else:
        abort(405, description='Only POST method')


def my_profile():
    return user_serv.my_profile()


def change_password():
    if request.method == 'POST':
        return user_serv.change_password(request)
    else:
        abort(405, description='Only POST method')


ctrl().register_methods(
    '/user/subscribe',
    'subscribe',
    create_user
)
ctrl().register(
    '/user/profile',
    'profile',
    my_profile
)
ctrl().register_methods(
    '/user/changepassword',
    'change_password',
    change_password
)
