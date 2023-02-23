from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service, auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            return "Вы не ввели данные"

        user_service.create(req_json)
        return "Пользователь добавлен", 201


@auth_ns.route('/login')
class AuthLogView(Resource):
    def post(self):
        req_json = request.json
        res = auth_service.authorization(req_json)
        return res


    def put(self):
        req_json = request.json
        res = auth_service.authorization_put(req_json)
        return res

