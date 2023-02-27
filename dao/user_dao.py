from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.get(uid)


    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user


    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.email = user_d.get("email")

        self.session.add(user)
        self.session.commit()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()
