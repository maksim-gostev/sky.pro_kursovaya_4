import pytest

from service.user_ser import UserService


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(user_dao)

    def test_get_one(self):
        users = self.user_service.get_one(1)
        assert users is not None
        assert users.id == 1
        assert users.email == 'email1'
        assert users.password == 'password1'
        assert users.name == 'name1'
        assert users.surname == 'surname1'
        assert users.favorite_genre == 1

    def test_get_by_email(self):
        users = self.user_service.get_one(1)
        assert users is not None
        assert users.id == 1
        assert users.email == 'email1'
        assert users.password == 'password1'
        assert users.name == 'name1'
        assert users.surname == 'surname1'
        assert users.favorite_genre == 1

    def test_create(self):
        data = {
            'id': 4,
            'email': 'email4',
            'password': 'password4',
            'name': 'name4',
            'surname': 'surname4',
            'favorite_genre': 4
        }

        user = self.user_service.create(data)
        assert user is not None
        assert user.id == 4
        assert user.email == 'email4'
        assert user.password == 'password4'
        assert user.name == 'name4'
        assert user.surname == 'surname4'
        assert user.favorite_genre == 4




    def tesr_get_user_by_token(self):
        users = self.user_service.get_one(1)
        assert users is not None
        assert users.id == 1
        assert users.email == 'email1'
        assert users.password == 'password1'
        assert users.name == 'name1'
        assert users.surname == 'surname1'
        assert users.favorite_genre == 1

