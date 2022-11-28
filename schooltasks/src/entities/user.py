"""moduli sisältää user-luokan"""


class User:
    """luokka käytäjän ominaisuuksille"""

    def __init__(self, first_name, last_name, user_id, passwd, teacher=False):
        """alustaa User luokan olion
        Args:   user_id: käyttäjätunnus, merkkijono
                password: salasana, merkkijono
                first_name: etunimi, merkkijono
                last_name: sukunimi, merkkijono
                teacher: onko opettaja, boolean"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.passwd = passwd
        self.teacher = teacher
