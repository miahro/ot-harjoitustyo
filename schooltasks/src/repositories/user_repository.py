"""sisältää luokan UserRepository"""

from entities.user import User
from dbcon import connection


class UserRepository:
    """luokka käyttäjän tietokantaoperaatiolle
    Attributes:
        _con: tietokantayhteys"""

    def __init__(self):
        """konstruktori alustaa tietokantayhteyden"""
        self._con = connection

    def add_user(self, user):
        """lisää uuden käyttjän tietokantaan
        Args
            user, User-luokan olio"""
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
        Args:
            user_id: käyttäjätunnus
        Returns:
            tietokantataulun pkid"""
        cursor = self._con.cursor()
        sql = """SELECT id
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchone() 

    def get_pwd(self, pk_id):
        """palauttaa salasanan käyttäjän primary id:n perusteella
        Args:
            pk_id: tietokantataulun käyttäjää vastaava pk id
        Returns:
            salasana (merkkijono"""
        cursor = self._con.cursor()
        sql = """SELECT passwd
                FROM Users
                WHERE id=:pk_id
                ;"""
        result = cursor.execute(sql, {"pk_id": pk_id})
        return result.fetchone()

    def get_pwd_by_user_id(self, user_id):
        """palauttaa salasanan käyttäjätunnuksen perusteella
        Args:
            user_id: käyttäjätunnus
        Returns:
            salasana: merkkijono"""
        cursor = self._con.cursor()
        sql = """SELECT passwd
                FROM Users
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchone()

    def user_details_by_user_id(self, user_id):
        """palauttaa käyttäjän etunimen, sukunimen, käyttjätunnuksen
        sekä tiedon onko opettaja käyttäjätunnuksen perusteella
        Args:
            user_id: käyttäjätunnus
        Returns:
            käyttäjätiedot (etunimi, sukunimi, käyttäjätunnus, onko opettaja)"""

        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, teacher
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchall()

    def user_by_user_id(self, user_id):
        """palauttaa User eli käyttäjäolion käyttäjätunnuksen perusteella
        Args:
            user_id käyttäjätunnus
        Returns:
            käyttäjätiedot sanakirjana
                keys, values:
                    first_name: etunimi
                    last_name: sukunimi
                    passwd: salasana
                    teacher: onko opettaja (boolean)"""
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, passwd, teacher
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id}).fetchone()
        if result is None:
            user = None
        else:
            user_dict = {"first_name": result[0],
                         "last_name": result[1],
                         "user_id": result[2],
                         "passwd": result[3],
                         "teacher": result[4]
                         }
            user = User(user_dict)
        return user

    def all_students(self):
        """hakee kaikkien opiskelijoiden tiedot:
        Returns:
            kaikkien opistekilijoiden tiedot listana (etunimi, sukunimi, käyttäjätunnus"""
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id
                FROM Users 
                WHERE teacher=FALSE
                ;"""
        result = cursor.execute(sql)
        return result.fetchall()

    def all_users(self):
        """hakee kaikkien käyttäjien tiedot
        Returns:
            kaikkien käyttäjien tiedot listana (etunimi, sukunimi, käyttäjätunnus, onko opettaja)"""
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
