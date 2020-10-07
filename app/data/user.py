import mongoengine as mong


class User(mong.Document):
    email = mong.EmailField()
    username = mong.StringField()
    password = mong.StringField()

    meta = {
        'strict': False,
    }
