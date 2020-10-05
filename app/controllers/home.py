from flask import request

from app.controllers import Controllers as ctrl
from app.constants import default_return


def index():
    return default_return, 200


ctrl().register(
    '/',
    'index',
    index
)
