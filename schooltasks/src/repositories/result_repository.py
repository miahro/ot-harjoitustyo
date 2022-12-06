"""sisälttää luokan ResultRepository"""

from dbcon import connection
#from entities.result import Result


class ResultRepository:
    """luokka tehtävien tietokantaoperaatiolle
    Attributes:
        _con: tietokantayhteys"""

    def __init__(self):
        """konstruktori"""
        self._con = connection

    # oma huomio: nyt tämä lisää uuden tulosrivin jos samaa tehtävää yritetään useammin
    # mietittävä mitä halutaan: pidetään yllä kaikki tulokset vai paras,
    # jolloin (person_id, task_id) yhdistelmä oltava unique, ja INSERTIN sijaan INSERT OR UPDATE
    def add_result(self, person_id, task_id, result):
        """lisää tieokantatauluun uuden tuloksen
        Args:
            person_id: henkilön pk id
            task_id: tehtävän ok id
            result: oikein/väärin (boolean)
        """
        cursor = self._con.cursor()
        sql = """INSERT INTO
                Results(person_id, task_id, result)
                Values(?,?,?) ON CONFLICT DO NOTHING"""
        cursor.execute(sql, (person_id, task_id, result))
        self._con.commit()

    def delete_all(self):
        """tuhoaa kaikki tiedot Result taulusta"""
        cursor = self._con.cursor()
        sql = """DELETE FROM Results"""
        cursor.execute(sql)
        self._con.commit()

    def get_user_total_correct(self, user_pkid):
        """hakee tietokannasta käyttäjän kaikkien oikeiden vastausten määrän
        Args:
            user_pkid: käyttäjän pkid tietokantataulussa
        Returns:
            käyttäjän oikeiden vastausten määrä (tuple 0-alkiona)
            """
        cursor = self._con.cursor()
        sql = """SELECT COUNT(*) FROM Results
                WHERE person_id=:user_pkid
                AND result=TRUE"""
        result = cursor.execute(sql, {"user_pkid": user_pkid})
        return result.fetchone()

    def get_user_total_fail(self, user_pkid):
        """hakee tietokannasta käyttäjän kaikkien väärien vastausten määrän
        Args:
            user_pkid: käyttäjän pkid tietokantataulussa
        Returns:
            käyttäjän väärien vastausten määrä (tuple 0-alkiona)
            """
        cursor = self._con.cursor()
        sql = """SELECT COUNT(*) FROM Results
                WHERE person_id=:user_pkid
                AND result=FALSE"""
        result = cursor.execute(sql, {"user_pkid": user_pkid})
        return result.fetchone()

    def get_user_all_correct(self, user_pkid):
        """hakee tietokannasta käyttäjän kaikki oikeat vastaukset
            summattuna per aihe per vaikeustaso
        Args:
            user_pkid: käyttäjän pkid tietokantataulussa
        Returns:
            käyttäjän oikeat vastaukset listana tupleja (aihe_id, vaikeustaso, kpl oikeita)
            """
        cursor = self._con.cursor()
        sql = """SELECT Tasks.topic_id, Tasks.difficulty, COUNT(result )
                FROM Results, Topics, Tasks
                WHERE
                    Results.person_id=1 AND
                    Results.result = TRUE AND
                    Results.task_id = Tasks.id AND
                    Tasks.topic_id = Topics.id
                    GROUP BY Tasks.topic_id, Tasks.difficulty; """
        result = cursor.execute(sql, {"user_pkid": user_pkid})
        return result.fetchall()

    def get_user_all_false(self, user_pkid):
        """hakee tietokannasta käyttäjän kaikki väärät vastaukset
            summattuna per aihe per vaikeustaso
        Args:
            user_pkid: käyttäjän pkid tietokantataulussa
        Returns:
            käyttäjän väärät vastaukset listana tupleja (aihe_id, vaikeustaso, kpl oikeita)
            """
        cursor = self._con.cursor()
        sql = """SELECT Tasks.topic_id, Tasks.difficulty, COUNT(result )
                FROM Results, Topics, Tasks
                WHERE
                    Results.person_id=1 AND
                    Results.result = FALSE AND
                    Results.task_id = Tasks.id AND
                    Tasks.topic_id = Topics.id
                    GROUP BY Tasks.topic_id, Tasks.difficulty; """
        result = cursor.execute(sql, {"user_pkid": user_pkid})
        return result.fetchall()


resultrepository = ResultRepository()
