from app.common import response as resp_comm
from app.repository import post as post_repo
from flask import abort
from flask_jwt import current_identity, jwt_required


@jwt_required()
def create_post(req):
    title = req.json['title']
    body = req.json['body']
    author = current_identity.id
    post = post_repo.create(
        title,
        body,
        author
    )
    if post:
        post_dto = post_repo.to_dto(post)
        return resp_comm.response(
            message='Post created',
            data={
                'post': post_dto
            }
        ), 201
    abort(500, description='Error while creating post')


@jwt_required()
def my_posts():
    posts = post_repo.find_by_author(current_identity.id)
    post_dtos = post_repo.list_to_dto(posts)
    return resp_comm.response(
        message='Posts retrieved',
        data={
            'posts': post_dtos
        }
    ), 200


@jwt_required()
def delete_post(post_id):
    post = post_repo.find(post_id)
    if post_repo.post_exists(post) is False:
        abort(404, description='Post does not exist anymore')
    if post.author.id == current_identity.id:
        post_repo.delete_post(post_id)
        return resp_comm.response(
            message='Post deleted'
        ), 200
    return resp_comm.response(
        success=False,
        message='Other user post'
    ), 200


@jwt_required()
def read_post(post_id):
    post = post_repo.find(post_id)
    if post:
        return resp_comm.response(
            message='Post found',
            data={
                'post': post_repo.to_dto(post)
            }
        ), 200
    return resp_comm.response(
        success=False,
        message='Post not found'
    ), 404


@jwt_required()
def update_post(req):
    post_id = req.json['id']
    new_title = req.json['title']
    new_body = req.json['body']
    updated_post = post_repo.modify_post(post_id, new_title, new_body)
    if updated_post:
        return resp_comm.response(
            data={
                'post': post_repo.to_dto(updated_post)
            }
        ), 200
    return resp_comm.response(
        success=False,
        message='Error while updating post'
    ), 200
