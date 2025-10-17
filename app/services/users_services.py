from repositories.users_repository import UserRepository

class UserService:
    @staticmethod
    def register_user(username, password, role="user"):
        if not username or not password:
            return {"msg": "username and password required"}, 400
        if UserRepository.find_by_username(username):
            return {"msg": "Username already exists"}, 400
        user = UserRepository.create_user(username, password, role=role)
        return {"msg": "User registered successfully", "username": user.username}, 201

    @staticmethod
    def authenticate_user(username, password):
        user = UserRepository.find_by_username(username)
        if not user:
            return None
        if not user.check_password(password):
            return None
        return user
