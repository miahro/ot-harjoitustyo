"""yksikkötestit UserServices luokalla"""
import unittest
from repositories.user_repository import userrepository
from services.user_services import userservices


class TestUserServices(unittest.TestCase):
    def setUp(self):
        userrepository.delete_all()
        self.userv = userservices
        self.userv.logout()

    def test_init(self):
        self.assertIsNotNone(self.userv)
        self.assertIsNone(self.userv.logged_in_user)

    def test_validate_inputs(self):
        self.assertEqual(self.userv.validate_inputs(
            ['nimi', 'sukunimi', 'tunnus', 'sala1', 'sala1']), True)

    def test_create_new_user(self):
        self.assertEqual(self.userv.create_new_user(
            'nimi', 'sukunimi', 'tunnus', 'sala1', 'sala1'), (True, 'käyttäjätunnus luotu'))

    def test_create_new_user_fail(self):
        self.assertEqual(self.userv.create_new_user(
            'nimi', '', 'tunnus', 'sala1', 'sala1'), (False, 'mikään kenttä ei saa olla tyhjä'))

    def test_create_new_user_fail2(self):
        self.assertEqual(self.userv.create_new_user(
            'nimi', 'sukunimi', 'tunnus', 'sala1', 'sala2'), (False, 'salasanat eroavat'))

    def test_create_new_user_fail3(self):
        self.userv.create_new_user(
            'nimi', 'sukunimi', 'tunnus', 'sala1', 'sala1')
        self.assertEqual(self.userv.create_new_user(
            'nimi', 'sukunimi', 'tunnus', 'sala1', 'sala1'), (False, 'käyttäjätunnus on jo olemassa'))

    def test_login(self):
        self.userv.create_new_user('nimi', 'suku', 'tunnus', 'sala1', 'sala1')
        self.assertEqual(self.userv.login("tunnus", "sala1"),
                         (True, "sisäänkirjautuminen käyttäjä tunnus onnistui"))

    def test_login_fail(self):
        self.userv.create_new_user('nimi', 'suku', 'tunnus', 'sala1', 'sala1')
        self.assertEqual(self.userv.login("tunnus", "sala"),
                         (False, "käyttäjätunnus ja salasana eivät täsmää"))

    def test_login_fail_no_user(self):
        self.userv.create_new_user('nimi', 'suku', 'tunnus', 'sala1', 'sala1')
        self.assertEqual(self.userv.login("tunnu", "sala1"),
                         (False, "käyttäjätunnusta ei löydy"))

    def test_logout(self):
        self.userv.create_new_user('nimi', 'suku', 'tunnus', 'sala1', 'sala1')
        self.userv.login("tunnus", "sala1")
        self.userv.logout()
        self.assertEqual(self.userv.logged_in_user, None)

    def test_active_user_details(self):
        self.userv.create_new_user(
            'nimi', 'sukunimi', 'tunnus', 'sala1', 'sala1')
        self.userv.login('tunnus', 'sala1')
        result = self.userv.active_user_details()
        self.assertEqual(result['first_name'], 'nimi')
        self.assertEqual(result['last_name'], 'sukunimi')
        self.assertEqual(result['user_id'], 'tunnus')
