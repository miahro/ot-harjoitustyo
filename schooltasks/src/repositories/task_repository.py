"""sisälttää luokan TaskRepository tehtävien tietokantaoperaatioille"""
import csv
import os.path
from dbcon import connection
from config import TASKS_INPUT_PATH, TASK_KEYS
from entities.task import Task


class TaskRepository:
    """luokka tehtävien tietokantaoperaatiolle
    Attributes:
        _con: tietokantayhteys"""

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

        Returns:
            tehtävät listana
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
        Args:
            tasks, lista tehtävistä muodossa [int, int, str, str, srt, str,str]
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

    def get_random_task_list(self, topic_id, difficulty, tasks_no):
        """palauttaa number_of_tasks määrän satunnaisia
        tehtävä-olioita listana
        Args:
            topic_id: aiheen tunniste
            difficulty: vaikeustaso
            tasks_no: palautettavien tehtävien määrä
        Returns:
            lista tehtävä-olioita"""
        cursor = self._con.cursor()
        sql = """SELECT topic_id,
                difficulty, 
                question,
                correct,
                wrong1,
                wrong2,
                wrong3, 
                id
                FROM Tasks 
                WHERE topic_id=:topic_id
                AND difficulty=:difficulty
                ORDER BY RANDOM() LIMIT :tasks_no
        """
        result = cursor.execute(
            sql, {"topic_id": topic_id, "difficulty": difficulty, "tasks_no": tasks_no})
        full_list = result.fetchall()
        keys = TASK_KEYS

        tasks_list_dict = [dict(zip(keys, values)) for values in full_list]
        tasks_list = [Task(x) for x in tasks_list_dict]
        return tasks_list

    def max_difficulty(self):
        """palauttaa maksimivaikeustason
        Returns:
            maksimivaikeuso tietokannassa (int)"""
        cursor = self._con.cursor()
        sql = "SELECT MAX(difficulty) FROM Tasks"
        result = cursor.execute(sql).fetchone()
        return result[0]

    def min_difficulty(self):
        """palauttaa minimivaikeustason
        Returns:
            minimivaikeustaso teitokannassa (int)"""
        cursor = self._con.cursor()
        sql = "SELECT MIN(difficulty) FROM Tasks"
        result = cursor.execute(sql).fetchone()
        return result[0]


taskrepository = TaskRepository()
