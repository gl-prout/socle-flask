from app.data.user import User


def user_exists(user):
    if user is None or user is False:
        return False
    return user


def create(email, username, password):
    user = User(
        email=email,
        username=username,
        password=password
    )
    user.save()
    return user


def find(identifier):
    user = User.objects(id=identifier).first()
    return user_exists(user)


def find_by_email(email):
    user = User.objects(email=email).first()
    return user_exists(user)


def find_by_username(username):
    user = User.objects(username=username).first()
    return user_exists(user)


def delete_by_id(identifier):
    user = User.objects(id=identifier).first()
    if user_exists(user):
        user.delete()


def delete_by_email(email):
    user = User.objects(email=email).first()
    if user_exists(user):
        user.delete()


def delete_by_username(username):
    user = User.objects(username=username).first()
    if user_exists(user):
        user.delete()


def find_all():
    users = User.objects()
    return list(users)


def to_dto(user):
    identifier = str(user.id)
    return {
        '_id': identifier,
        'email': user.email,
        'username': user.username,
    }


def list_to_dto(users):
    results = []
    for user in users:
        results.append(to_dto(user))
    return results
