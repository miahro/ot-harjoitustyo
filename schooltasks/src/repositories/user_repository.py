"""sisältää luokan UserRepository"""

from entities.user import User
from dbcon import connection


class UserRepository:
    """luokka käyttäjän tietokantaoperaatiolle"""

    def __init__(self):
        """konstruktori alustaa tietokantayhteyden"""
        self._con = connection

    def add_user(self, user):
        """lisää uuden käyttjän tietokantaan
        Args    user, User-luokan olio"""
        cursor = self._con.cursor()
        sql = """INSERT OR IGNORE INTO
            Users(first_name, last_name, user_id, passwd, teacher)
            VALUES(:first_name, :last_name, :user_id, :passwd, :teacher)
            ON CONFLICT DO NOTHING        
        ;"""
        cursor.execute(sql, {"first_name": user.first_name, "last_name": user.last_name,
                       "user_id": user.user_id, "passwd": user.passwd, "teacher": user.teacher})
        self._con.commit()

    def get_pk_id(self, user_id):
        """plauttaa tietokantataulun primary id:n user_id:n perusteella
        Args user_id: käyttäjätunnus"""
        cursor = self._con.cursor()
        sql = """SELECT id
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchone()

    def get_pwd(self, pk_id):
        """palauttaa salasanan käyttäjän primary id:n perusteella
        Args pk_id: tietokantataulun käyttäjää vastaava pk id"""
        cursor = self._con.cursor()
        sql = """SELECT passwd
                FROM Users
                WHERE id=:pk_id
                ;"""
        result = cursor.execute(sql, {"pk_id": pk_id})
        return result.fetchone()

    def get_pwd_by_user_id(self, user_id):
        """palauttaa salasanan käyttäjän käyttäjätunnuksen perusteella
        Args  user_id: käyttäjätunnus"""
        cursor = self._con.cursor()
        sql = """SELECT passwd
                FROM Users
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchone()

    def user_details_by_user_id(self, user_id):
        """palauttaa käytjän etunimen, sukunimen, käyttjätunnuksen
        sekä tiedon onko opettaja käyttäjätunnuksen perusteella
        Args    user_id: käyttäjätunnus"""

        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, teacher
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchall()

    def user_by_user_id(self, user_id):
        """palauttaa User eli käyttäjäolion käyttäjätunnuksen perusteella
        Args   user_id käyttäjätunnus"""
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, passwd, teacher
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id}).fetchone()
        if result is None:
            user = None
        else:
            user = User(result[0], result[1], result[2], result[3])
        return user

    def all_students(self):
        """palautttaa kaikkien opiskelijoiden etunimet, sukunimet ja käyttjätunnukset"""
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id
                FROM Users 
                WHERE teacher=FALSE
                ;"""
        result = cursor.execute(sql)
        return result.fetchall()

    def all_users(self):
        """palauttaa kaikkien käyttäjien etunimet, sukunimet,
        käyttäjätunnukset ja tiedon onko opettaja"""
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, teacher
                FROM Users 
                ;"""
        result = cursor.execute(sql)
        return result.fetchall()

    def delete_all(self):
        """"poistaa kaikki tiedot tietokannan Users taulusta"""
        cursor = self._con.cursor()
        sql = """DELETE FROM Users"""
        cursor.execute(sql)
        self._con.commit()


userrepository = UserRepository()
