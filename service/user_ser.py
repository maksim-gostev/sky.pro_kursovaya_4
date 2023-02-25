import hashlib

import jwt

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET, ALGO
from dao.user_dao import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)



    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def patch(self, token, data):
        user = self.get_user_by_token(token)

        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')

        return self.dao.update(user)

    def get_user_by_token(self, data):
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, SECRET, algorithms=[ALGO])
            uid = user.get('id')
        except Exception as e:
            print("JWT Decode Exception", e)

        return self.get_one(uid)

    def update_password(self, token, password):
        if password["password_1"] == password["password_2"]:
            user = self.get_user_by_token(token)
            user.password = self.get_hash(password["password_1"])
            return self.dao.update(user)