import jwt
from flask import request, abort

from constants import SECRET, ALGO


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[ALGO])
        except Exception as e:
            print(f'Ошибка доступа: {e}')
            abort(401)
        return func(*args, **kwargs)

    return wrapper
