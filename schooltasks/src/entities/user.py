"""moduli sisältää user-luokan"""


class User:
    """luokka käytäjän ominaisuuksille
    Attributes:
        user_id: käyttäjätunnus, merkkijono
        password: salasana, merkkijono
        first_name: etunimi, merkkijono
        last_name: sukunimi, merkkijono
        teacher: onko opettaja, boolean"""

    def __init__(self, user_dict, teacher=False):
        """alustaa User luokan olion
        Args:   user_dict
                keys, values    user_id: käyttäjätunnus, merkkijono
                                password: salasana, merkkijono
                                first_name: etunimi, merkkijono
                                last_name: sukunimi, merkkijono
                                teacher: onko opettaja, boolean"""
        self.first_name = user_dict["first_name"]
        self.last_name = user_dict["last_name"]
        self.user_id = user_dict["user_id"]
        self.passwd = user_dict["passwd"]
        self.teacher = teacher

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.user_id}, "\
            f"{self.passwd}, {self.teacher})"

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, "\
            f"user_id: {self.user_id}, passwd: {self.passwd}, teacher: {self.teacher}"
