from flask_restx import Resource, Namespace
from flask import request

from dao.model.user import UserSchema
from implemented import user_service
from service.decorators import auth_required

user_ns = Namespace('users')

user_schema = UserSchema()


@user_ns.route('')
class UsersView(Resource):
    @auth_required
    def get(self):
        auth_data = request.headers['Authorization']
        user = user_service.get_user_by_token(auth_data)
        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        auth_data = request.headers['Authorization']
        req_json = request.json
        user = user_service.patch(auth_data, req_json)
        return user_schema.dump(user)


@user_ns.route('/password/')
class PasswordView(Resource):
    @auth_required
    def put(self):
        auth_data = request.headers['Authorization']
        passwords = request.json
        user = user_service.update_password(auth_data, passwords)
        return user_schema.dump(user)
