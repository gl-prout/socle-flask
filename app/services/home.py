from flask.helpers import send_from_directory
from app.constants import default_return


def hello():
    return default_return, 200


def api(filename):
    return send_from_directory('api', filename)
