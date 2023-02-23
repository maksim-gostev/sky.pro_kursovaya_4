from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.email = user_d.get("email")

        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()
