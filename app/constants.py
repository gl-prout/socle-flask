from . import app
from app.common import response as resp_common

configs = app.config
name = app
default_return = resp_common.response(
    success=True,
    message='Awaiting API calls',
    data={
        'version': '1.0',
    }
)
