def response(success=True, message='Success', data=None):
    if data is None:
        data = {}
    return {
        'success': success,
        'message': message,
        'data': data,
    }
