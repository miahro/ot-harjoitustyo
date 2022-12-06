"""moduuli sisältää TopicRepository -luokan"""
import csv
import os.path
from dbcon import connection
from config import TOPICS_INPUT_PATH


class TopicRepository:
    """luokka käyttäjän tietokantaoperaatiolle
    Attributes:
        _con: tietokantayhteys"""

    def __init__(self):
        """konstruktori"""
        self._con = connection

    @staticmethod
    def check_file_path():
        """tarkistaa onko aihe-tiedosta ja polku olemassa"""
        return os.path.exists(TOPICS_INPUT_PATH)

    def read_from_file(self):
        """lukee aiheet CSV tiedostosta
        Returns:
            aiheet listana (merkkijonoja)"""
        if not self.check_file_path():
            return []
        tops = []
        with open(TOPICS_INPUT_PATH, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for line in csv_reader:
                tops.append((line[0],))
        return tops

    def update_db(self, topics):
        """lisää tieokantatauluun uudet aiheet
        Args:
            topics: lista aiheita (merkkijonoja)"""
        cursor = self._con.cursor()
        sql = """INSERT INTO
                Topics(topic)
                Values(?) ON CONFLICT DO NOTHING"""
        cursor.executemany(sql, topics)
        self._con.commit()

    def all_topics(self):
        """palauttaa kaikkien aiheiden nimet
        Returns:
            lista aiheista (merkkijonoja)"""
        cursor = self._con.cursor()
        sql = """SELECT topic
                FROM Topics"""
        query = cursor.execute(sql).fetchall()
        result = [item[0] for item in query]
        return result

    def id_by_topic(self, topic):
        """palauttaa tietokantataulun pk id:n aiheen perusteella
        palauttaa 0 jos ei löydy
        Args:
            topic, aihe mekkijonona
        Returns:
            aiheen tietokannan pkid (0, jos ei löydy)
        """
        cursor = self._con.cursor()
        sql = """SELECT id
                FROM Topics
                WHERE topic=?;"""
        query = cursor.execute(sql, (topic,)).fetchone()
        return query[0]

    def topic_by_id(self, topic_id):
        """palauttaa aiheen nimen tietokantataulun pk id:n perusteella
        palauttaa tyhjän merkkijonon, jos ei löydy
        Args:
            id, kokonaisluku
        Returns:
            aiheen nimi (merkkijono), tyhjä jos ei löydy """
        cursor = self._con.cursor()
        sql = """SELECT Topic
                FROM Topics
                WHERE id =?;"""
        query = cursor.execute(sql, (topic_id,)).fetchone()
        if query:
            return query[0]
        return ""

    def delete_all(self):
        """poistaa kaikki tiedot Topics tietokantataulusta"""
        cursor = self._con.cursor()
        sql = """DELETE FROM Topics"""
        cursor.execute(sql)
        self._con.commit()

topicrepository = TopicRepository()
