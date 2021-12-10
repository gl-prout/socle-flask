import mongoengine as mong

from app.data.user import User


class Post(mong.Document):
    title = mong.StringField()
    body = mong.StringField()
    author = mong.ReferenceField(User)
    created_at = mong.DateTimeField()

    meta = {
        'strict': False,
    }
