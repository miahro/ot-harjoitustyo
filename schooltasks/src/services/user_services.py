"""sisältää luokan UserServices"""

from entities.user import User
from repositories.user_repository import userrepository


class UserServices:
    """Luokka käyttäjän palveluita varten"""

    def __init__(self):
        """konstruktori alustaa tyhjän olion, ja käyttäää userrepository oliota"""
        self.logged_in_user = None
        self.user_repository = userrepository
        self.user = None  # ei käytetä toistaiseksi mihinkään

    def create_new_user(self, first_name, last_name, user_id, passwd1, passwd2, teacher=False):
        """luo uuden käyttäjän, ja lisää käyttäjän tiedot tietokantaan
        palauttaa tuplen (True/False, viesti)
        Args    first_name: etunimi, st
                last_name: sukunimi, str
                user_id: käyttäjätunnus, str
                passwd1: salasana, str
                passwd2: salasana, str (uudelleen syötetetty salasana luontitarkistusta varte)
                teachedr: bool, default=False, onko opettaja vai oppilas
                """
        if not self.validate_inputs([first_name, last_name, user_id, passwd1, passwd2]):
            return (False, "mikään kenttä ei saa olla tyhjä")
        if passwd1 != passwd2:
            return (False, "salasanat eroavat")
        user_dict = {"first_name":first_name,
                    "last_name": last_name,
                    "user_id": user_id,
                    "passwd": passwd1,
                    "teacher": teacher
                    }
        self.user = User(user_dict)
        if len(self.user_repository.user_details_by_user_id(self.user.user_id)) != 0:
            return (False, "käyttäjätunnus on jo olemassa")
        self.user_repository.add_user(self.user)
        return (True, "käyttäjätunnus luotu")

    @staticmethod
    def validate_inputs(lst):
        """tarksistaa, ettei mikään tekstimuotoinen syöte ole tyhjä
        Args: [lst], lista tekstimuotoisia syötteitä"""
        for item in lst:
            if len(item) == 0:
                return False
        return True

    def login(self, user_id, passwd):
        """kirjaa käyttäjän sisään
        palauttaa tuplen (True/False, viesti)
        Args    user_id: käyttäjätunnus
                passwd: salasana"""
        password = self.user_repository.get_pwd_by_user_id(user_id)
        if password is None:
            return (False, "käyttäjätunnusta ei löydy")
        if password[0] != passwd:
            return (False, "käyttäjätunnus ja salasana eivät täsmää")
        self.logged_in_user = self.user_repository.user_by_user_id(user_id)
        return (True, f"sisäänkirjautuminen käyttäjä {user_id} onnistui")

    def logout(self):
        """kirjaa käyttäjän ulos"""
        self.logged_in_user = None

    def active_user_details(self):
        """palauttaa sisäänkirjautuneen käyttäjän tiedot"""
        user_details = {}
        user_details['first_name'] = self.logged_in_user.first_name
        user_details['last_name'] = self.logged_in_user.last_name
        user_details['user_id'] = self.logged_in_user.user_id

        return user_details


userservices = UserServices()
