"""yksikkötestit ResultServicesluokalle"""
import unittest
from config import DB_FILE, DB_FILE_PATH, TASKS_INPUT_PATH
from services.user_services import userservices
from repositories.topic_repository import topicrepository
from services.task_services import taskservices
from services.result_services import ResultServices


class TestResultServices(unittest.TestCase):
    def setUp(self):

        taskservices.update_tasks_db()
        self.resultservices = ResultServices()
        self.resultservices.delete_all()
        self.userservices = userservices
        self.userservices.create_new_user(
            "testi", "käyttäjä", "testitunnus", "sala", "sala", teacher=False)

        topicrepository.update_db(topicrepository.read_from_file())

    def test_add_result(self):
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["total_tasks"], 0)
        self.resultservices.add_result("testitunnus", 1, False)
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["total_tasks"], 1)
        self.resultservices.delete_all()

    def test_user_totals(self):
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["total_tasks"], 0)
        self.resultservices.add_result("testitunnus", 1, False)
        self.resultservices.add_result("testitunnus", 2, False)
        self.resultservices.add_result("testitunnus", 3, True)
        self.resultservices.add_result("testitunnus", 4, True)
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["total_tasks"], 4)
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["correct"], 2)
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["fail"], 2)
        self.assertEqual(self.resultservices.user_totals(
            "testitunnus")["correct_percent"], 50)
        self.resultservices.delete_all()

    def test_user_details(self):
        self.resultservices.add_result("testitunnus", 1, False)
        self.resultservices.add_result("testitunnus", 2, False)
        self.resultservices.add_result("testitunnus", 3, True)
        self.resultservices.add_result("testitunnus", 4, True)
        result = self.resultservices.user_details("testitunnus")
        self.assertEqual(list(result.keys()), ['all', 'correct', 'fail'])
        self.assertEqual(list(result['all'].keys()), [
                         'yhteenlasku', 'vähennyslasku', 'kertolasku', 'jakolasku'])
        self.assertEqual(list(result['correct'].keys()), [
                         'yhteenlasku', 'vähennyslasku', 'kertolasku', 'jakolasku'])
        self.assertEqual(list(result['fail'].keys()), [
                         'yhteenlasku', 'vähennyslasku', 'kertolasku', 'jakolasku'])

    def test_user_results_by_topic(self):
        self.resultservices.add_result("testitunnus", 1, False)
        self.resultservices.add_result("testitunnus", 2, False)
        self.resultservices.add_result("testitunnus", 3, True)
        self.resultservices.add_result("testitunnus", 4, True)
        result = self.resultservices.user_results_by_topic(
            "testitunnus", "yhteenlasku")
        if result:
            self.assertEqual(result['topic'], 'yhteenlasku')
            self.assertEqual(result['correct'], 2)
            self.assertEqual(result['fail'], 2)
            self.assertEqual(result['total_tasks'], 4)

    def test_user_results_by_topic_all_topics(self):
        self.resultservices.add_result("testitunnus", 1, False)
        self.resultservices.add_result("testitunnus", 2, False)
        self.resultservices.add_result("testitunnus", 3, True)
        self.resultservices.add_result("testitunnus", 4, True)
        result = self.resultservices.user_results_by_topic_all_topics(
            "testitunnus")
        self.assertEqual(result[0]['topic'], 'yhteenlasku')
        self.assertEqual(result[0]['correct'], 2)
        self.assertEqual(result[0]['fail'], 2)
        self.assertEqual(result[0]['total_tasks'], 4)
