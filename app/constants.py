from . import app

configs = app.config
name = app
default_return = {
    'status': 'success',
    'message': 'Parcel pending API',
    'data': {
        'version': '1',
    },
}
