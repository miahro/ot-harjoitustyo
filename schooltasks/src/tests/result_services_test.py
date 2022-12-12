"""yksikkötestit ResultServicesluokalle"""
import unittest
from os.path import isfile
from config import DB_FILE, DB_FILE_PATH
from dbcon import connection
from entities.user import User
from services.user_services import userservices
from repositories.topic_repository import topicrepository
from services.result_services import ResultServices, resultservices


class TestResultServices(unittest.TestCase):
    def setUp(self):
        self.resultservices = ResultServices()
        self.resultservices.delete_all()
        self.userservices=userservices
        self.userservices.create_new_user("tesi", "käyttäjä", "testitunnus", "sala", "sala", teacher=False)


    def test_add_result(self):
        self.assertEqual(self.resultservices.user_totals("testitunnus")["total_tasks"], 0)
        self.resultservices.add_result("testitunnus", 1, False)
        self.assertEqual(self.resultservices.user_totals("testitunnus")["total_tasks"], 1)
        
    def test_user_totals(self):
        self.assertEqual(self.resultservices.user_totals("testitunnus")["total_tasks"], 0)
        self.resultservices.add_result("testitunnus", 1, False)
        self.resultservices.add_result("testitunnus", 2, False)
        self.resultservices.add_result("testitunnus", 3, True)
        self.resultservices.add_result("testitunnus", 4, True)
        self.assertEqual(self.resultservices.user_totals("testitunnus")["total_tasks"], 4)
        self.assertEqual(self.resultservices.user_totals("testitunnus")["correct"], 2)
        self.assertEqual(self.resultservices.user_totals("testitunnus")["fail"], 2)
        self.assertEqual(self.resultservices.user_totals("testitunnus")["correct_percent"], 50)


    def test_user_details(self):
        pass
        #ei testaa vielä mitään

    def test_delete_all(self):
        pass
        #ei testaa vielä mitään

