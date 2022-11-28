"""yksikkötestit UserRepository luokalla"""
import unittest
from os.path import isfile
from config import DB_FILE, DB_FILE_PATH
from dbcon import connection
from entities.user import User
from repositories.user_repository import userrepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        userrepository.delete_all()
        self.test_student = User(
            first_name='Tero', last_name='Testi', user_id='tt1', passwd='xx')
        self.test_student2 = User(
            first_name='Taavi', last_name='Toinen', user_id='tt2', passwd='xx')
        self.test_teacher = User(
            first_name='Olli', last_name='Ope', user_id='maikka', passwd='yy', teacher=True)

    def test_DB_exists(self):
        # print(DB_FILE_PATH)
        self.assertEqual(isfile(DB_FILE_PATH), True)

    def test_table_exists(self):
        self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Users';").fetchone()[0], 1)
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Topics';").fetchone()[0], 1)
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Tasks';").fetchone()[0], 1)
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Results';").fetchone()[0], 1)

    def test_add_user(self):
        size0 = connection.execute("SELECT COUNT(*) FROM Users;").fetchone()[0]
        userrepository.add_user(self.test_student)
        size1 = connection.execute("SELECT COUNT(*) FROM Users;").fetchone()[0]
        self.assertEqual(size1-size0, 1)

    def test_all_students(self):
        userrepository.add_user(self.test_student)
        userrepository.add_user(self.test_student2)
        students = userrepository.all_students()
        print(students)
        self.assertEqual(students[0], ('Tero', 'Testi', 'tt1'))
        self.assertEqual(students[1], ('Taavi', 'Toinen', 'tt2'))
        self.assertEqual(len(students), 2)

    def test_all_users(self):
        userrepository.add_user(self.test_student)
        userrepository.add_user(self.test_student2)
        userrepository.add_user(self.test_teacher)
        students = userrepository.all_users()
        self.assertEqual(students[0], ('Tero', 'Testi', 'tt1', 0))
        self.assertEqual(students[1], ('Taavi', 'Toinen', 'tt2', 0))
        self.assertEqual(students[2], ('Olli', 'Ope', 'maikka', 1))
        self.assertEqual(len(students), 3)

    def test_user_details_by_user_id(self):
        userrepository.add_user(self.test_student)
        student = userrepository.user_details_by_user_id("tt1")
        self.assertEqual(student[0],  ('Tero', 'Testi', 'tt1', 0))

    def test_get_pwd(self):
        userrepository.add_user(self.test_student)
        id = userrepository.get_pk_id("tt1")[0]
        pwd = userrepository.get_pwd(id)
        self.assertEqual(pwd[0], "xx")

    def test_get_pwd_by_user_id(self):
        userrepository.add_user(self.test_student)
        pwd = userrepository.get_pwd_by_user_id(self.test_student.user_id)
        self.assertEqual(pwd[0], "xx")

    def test_get_pwd_by_user_id_fail(self):
        pwd = userrepository.get_pwd_by_user_id(0)
        self.assertEqual(pwd, None)

    def test_user_by_user_id(self):
        userrepository.add_user(self.test_student)
        user = userrepository.user_by_user_id("tt1")
        self.assertEqual(user.first_name, self.test_student.first_name)
