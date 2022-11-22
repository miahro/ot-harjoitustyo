#from entities.user import User
from dbcon import connection

class UserRepository:
    """luokka käyttäjän tietokantaoperaatiolle"""

    def __init__(self):
        """konstruktori"""

        self._con = connection

    def add_user(self, user):
        cursor = self._con.cursor()
        sql = """INSERT OR IGNORE INTO
            Users(first_name, last_name, user_id, passwd, teacher)
            VALUES(:first_name, :last_name, :user_id, :passwd, :teacher)
            ON CONFLICT DO NOTHING        
        ;"""
        cursor.execute(sql, {"first_name": user.first_name, "last_name": user.last_name, "user_id": user.user_id, "passwd": user.passwd, "teacher": user.teacher})
        self._con.commit()

    def get_pk_id(self, user_id):
        cursor = self._con.cursor()
        sql = """SELECT id
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchone()[0]

    def get_pwd(self, pk_id):
        cursor = self._con.cursor()
        sql = """SELECT passwd
                FROM Users
                WHERE id=:pk_id
                ;"""
        result = cursor.execute(sql, {"pk_id": pk_id})
        return result.fetchone()[0]

    def user_details_by_user_id(self, user_id):
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, teacher
                FROM Users 
                WHERE user_id=:user_id
                ;"""
        result = cursor.execute(sql, {"user_id": user_id})
        return result.fetchall()

    def all_students(self):
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id
                FROM Users 
                WHERE teacher=FALSE
                ;"""
        result = cursor.execute(sql)
        return result.fetchall()

    def all_users(self):
        cursor = self._con.cursor()
        sql = """SELECT first_name, last_name, user_id, teacher
                FROM Users 
                ;"""
        result = cursor.execute(sql)
        return result.fetchall()

    def delete_all(self):
        cursor = self._con.cursor()
        sql ="""DELETE FROM Users"""
        cursor.execute(sql)
        self._con.commit()

userrepository = UserRepository()
