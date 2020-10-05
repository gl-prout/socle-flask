def response(success=True, message='Success', data={}):
    return {
        'success': success,
        'message': message,
        'data': data,
    }
