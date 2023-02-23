import calendar
import datetime

import jwt
from flask import abort

from constants import SECRET, ALGO
from service.user_ser import UserService

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def authorization(self, data) -> dict:
        username = data.get('username', None)
        password = data.get('password', None)

        if None in [username, password]:
            abort(400)
        user = self.user_service.get_by_username(username)
        if user is None:
            return {"error": "Нет такого юзера"}, 401

        password_hash = self.user_service.get_hash(password)

        if password_hash != user.password:
            return {"error": "Неверный пороль"}, 401

        tokens = self.get_tokens(user)
        return tokens




    def authorization_put(self, req_json):
        refresh_token = req_json.get('refresh_token', )
        if refresh_token is None:
            abort(400)

        try:
            data = jwt
        except Exception:
            abort(400)

        username = data.get('username')

        user = self.user_service.get_by_username(username)

        tokens = self.get_tokens(user)
        return tokens




    def get_tokens(self, user):
        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens, 201