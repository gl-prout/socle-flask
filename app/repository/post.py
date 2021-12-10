from datetime import datetime

from app.data.post import Post


def post_exists(post):
    if post is None or post is False:
        return False
    return post


def create(title, body, author):
    post = Post(
        title=title,
        body=body,
        author=author
    )
    post.created_at = datetime.now()
    post.save()
    return post_exists(post)


def find(identifier):
    post = Post.objects(id=identifier).first()
    return post_exists(post)


def find_by_author(user):
    posts = Post.objects(author=user).order_by('-id')
    if posts:
        return posts
    return []


def modify_post(identifier, new_title, new_body):
    post = Post.objects(id=identifier).first()
    if (post_exists(post)):
        post.title = new_title
        post.body = new_body
        post.save()
        return post;
    return False


def delete_post(identifier):
    post = Post.objects(id=identifier).first()
    if post_exists(post):
        post.delete()


def find_all():
    posts = Post.objects()
    return list(posts)


def to_dto(post):
    identifier = str(post.id)
    return {
        '_id': identifier,
        'title': post.title,
        'body': post.body,
        'created_at': int(datetime.timestamp(post.created_at)),
        'author': post.author.username,
    }


def list_to_dto(posts):
    results = []
    for post in posts:
        results.append(to_dto(post))
    return results
