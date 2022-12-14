"""yksikkötestit QuestionGenerator luokalle"""
import unittest
import os
from config import TASKS_INPUT_PATH

from question_generator import QuestionGenerator


class TestQuestionGenerator(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(TASKS_INPUT_PATH):
            os.remove(TASKS_INPUT_PATH)
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

    def test_division(self):
        self.test_question_generator.division()
        with open(self.test_question_generator.filepath, 'r', encoding='utf-8') as test:
            final_line = test.readlines()[-1]
        final_line_list = final_line.split(';')
        print(final_line_list[0])
        self.assertEqual(final_line_list[0], '4')
        self.assertTrue(final_line_list[1].isdigit())
        self.assertIn("jakolaskun", final_line_list[2])
        self.assertIn("oikea", final_line_list[2])
        self.assertIn("jakojäännös", final_line_list[3])
        self.assertIn("osamäärä", final_line_list[3])
        self.assertIn("jakojäännös", final_line_list[4])
        self.assertIn("osamäärä", final_line_list[4])
        self.assertIn("jakojäännös", final_line_list[5])
        self.assertIn("osamäärä", final_line_list[5])
        self.assertIn("jakojäännös", final_line_list[6])
        self.assertIn("osamäärä", final_line_list[6])
