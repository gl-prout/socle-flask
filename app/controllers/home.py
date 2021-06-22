from app.controllers import Controllers as ctrl
from app.services import home as home_serv
from flask import abort, request


def index():
    if request.method == 'GET':
        return home_serv.hello()
    else:
        abort(405, description='Only GET method')


def getapi(filename):
    if request.method == 'GET':
        return home_serv.api(filename)
    else:
        abort(405, description='Only GET method')


ctrl().register_methods(
    '/',
    'index',
    index
)
ctrl().register_methods(
    '/apidoc/<path:filename>',
    'getapi',
    getapi
)
