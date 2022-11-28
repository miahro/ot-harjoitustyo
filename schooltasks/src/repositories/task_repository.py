"""sisälttää luokan TaskRepository tehtävien tietokantaoperaatioille"""
import csv
import os.path
from dbcon import connection
from config import TASKS_INPUT_PATH
#from entities.task import Task


class TaskRepository:
    """luokka tehtävien tietokantaoperaatiolle"""

    def __init__(self):
        """konstruktori"""
        self._con = connection

    @staticmethod
    def check_file_path():
        """tarkistaa onko tehtävät tiedosto ja polku olemassa"""
        return os.path.exists(TASKS_INPUT_PATH)

    def read_from_file(self):
        """lukee tehtävät CSV tiedostosta
        palauttaa tehtävät listana
        """
        if not self.check_file_path():
            return []
        tasks = []
        with open(TASKS_INPUT_PATH, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            for line in csv_reader:
                tasks.append(line)
        return tasks

    def update_db(self, tasks):
        """lisää tieokantatauluun uudet aiheet
        Args: tasks, lista tehtävistä
        lista on [int, int, str, str, srt, str,str]
        """
        cursor = self._con.cursor()
        sql = """INSERT INTO
                Tasks(topic_id, difficulty, question, correct, wrong1, wrong2, wrong3)
                Values(?,?,?,?,?,?,?) ON CONFLICT DO NOTHING"""
        for task in tasks:
            cursor.execute(sql, task)
            self._con.commit()

    def delete_all(self):
        """tuhoaa kaikki tehtävät tietokantataulusta"""
        cursor = self._con.cursor()
        sql = """DELETE FROM Tasks"""
        cursor.execute(sql)
        self._con.commit()


# tämä luokka ei ole valmis, tarvitaan lisää hakutoimintoja

taskrepository = TaskRepository()
