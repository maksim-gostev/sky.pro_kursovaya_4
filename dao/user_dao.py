from dao.model.user import User
from dao.base import BaseDAO


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user


    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()
