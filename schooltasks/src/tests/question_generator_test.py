"""yksikkötestit QuestionGenerator luokalle"""
import unittest
from entities.user import User
from repositories.user_repository import userrepository
from services.user_services import userservices
from question_generator import QuestionGenerator


class TestQuestionGenerator(unittest.TestCase):
    def setUp(self):
        self.test_question_generator = QuestionGenerator()

    def test_addition(self):
        self.test_question_generator.addition()
        with open(self.test_question_generator.filepath, 'r', encoding='utf-8') as test:
            final_line = test.readlines()[-1]
        final_line_list = final_line.split(';')
        self.assertEqual(final_line_list[0], '1')
        self.assertTrue(final_line_list[1].isdigit())
        self.assertIn("yhteenlaskun", final_line_list[2])
        self.assertTrue(final_line_list[3].isdigit())
        self.assertTrue(final_line_list[4].isdigit())
        self.assertTrue(final_line_list[5].isdigit())
        self.assertTrue(final_line_list[6].strip().isdigit())

    def test_subtraction(self):
        self.test_question_generator.subtraction()
        with open(self.test_question_generator.filepath, 'r', encoding='utf-8') as test:
            final_line = test.readlines()[-1]
        final_line_list = final_line.split(';')
        self.assertEqual(final_line_list[0], '2')
        self.assertTrue(final_line_list[1].isdigit())
        self.assertIn("vähennyslaskun", final_line_list[2])
        self.assertTrue(final_line_list[3].lstrip('-').isdigit())
        self.assertTrue(final_line_list[4].lstrip('-').isdigit())
        self.assertTrue(final_line_list[5].lstrip('-').isdigit())
        self.assertTrue(final_line_list[6].strip().lstrip('-').isdigit())

    def test_multiplication(self):
        self.test_question_generator.multiplication()
        with open(self.test_question_generator.filepath, 'r', encoding='utf-8') as test:
            final_line = test.readlines()[-1]
        final_line_list = final_line.split(';')
        self.assertEqual(final_line_list[0], '3')
        self.assertTrue(final_line_list[1].isdigit())
        self.assertIn("kertolaskun", final_line_list[2])
        self.assertTrue(final_line_list[3].isdigit())
        self.assertTrue(final_line_list[4].isdigit())
        self.assertTrue(final_line_list[5].isdigit())
        self.assertTrue(final_line_list[6].strip().isdigit())
