from entities.user import User
from repositories.user_repository import userrepository


class UserServices:
    def __init__(self):
        self.logged_in_user = None
        self.user_repository = userrepository
        self.user = None

    def create_new_user(self, first_name, last_name, user_id, passwd1, passwd2, teacher=False):

        if not self.validate_inputs([first_name, last_name, user_id, passwd1, passwd2]):
            return (False, "mikään kenttä ei saa olla tyhjä")
        if passwd1 != passwd2:
            return (False, "salasanat eroavat")
        self.user = User(first_name, last_name, user_id,
                         passwd1, teacher=False)
        if len(self.user_repository.user_details_by_user_id(self.user.user_id)) != 0:
            return (False, "käyttäjätunnus on jo olemassa")
        self.user_repository.add_user(self.user)
        return (True, "käyttäjätunnus luotu")

    @staticmethod
    def validate_inputs(lst):
        for item in lst:
            if len(item) == 0:
                return False
        return True

    def login(self, user_id, passwd):
        password = self.user_repository.get_pwd_by_user_id(user_id)
        if password[0] != passwd:
            return (False, "käyttäjätunnus ja salasana eivät täsmää")
        self.logged_in_user = self.user_repository.user_by_user_id(user_id)
        return (True, f"sisäänkirjautuminen käyttäjä {user_id} onnistui")

    def logout(self):
        self.logged_in_user = None


userservices = UserServices()
