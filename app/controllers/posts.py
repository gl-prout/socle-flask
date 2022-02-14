from app.controllers import Controllers as Ctrl
from app.services import posts as post_serv
from flask import abort, request


def create_post():
    if request.method == 'POST':
        return post_serv.create_post(request)
    else:
        abort(405, description='Only POST method')


def my_posts():
    return post_serv.my_posts()


def update_post():
    if request.method == 'PUT':
        return post_serv.update_post(request)
    else:
        abort(405, description='Only PUT method')


def action_post(post_id):
    if request.method == 'DELETE':
        return post_serv.delete_post(post_id)
    elif request.method == 'GET':
        return post_serv.read_post(post_id)
    else:
        abort(405, description='Only GET or DELETE method')


Ctrl().register(
    '/posts/mine',
    'my_posts',
    my_posts
)
Ctrl().register_methods(
    '/posts/create',
    'create_post',
    create_post
)
Ctrl().register_methods(
    '/posts/update',
    'update_post',
    update_post
)
Ctrl().register_methods(
    '/posts/<string:post_id>',
    'action_post',
    action_post
)
