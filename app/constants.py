from app.common import response as resp_common

from . import app

configs = app.config
name = app
default_return = resp_common.response(
    success=True,
    message='Awaiting API calls',
    data={
        'version': '1.1.0',
    }
)
