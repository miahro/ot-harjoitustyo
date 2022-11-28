from dbcon import connection
from entities.result import Result


class ResultRepository:
    """luokka tehtävien tietokantaoperaatiolle"""

    def __init__(self):
        """konstruktori"""
        self._con = connection

    # oma huomio: nyt tämä lisää uuden tulosrivin jos samaa tehtävää yritetään useammin
    # mietittävä mitä halutaan: pidetään yllä kaikki tulokset vai paras,
    # jolloin (person_id, task_id) yhdistelmä oltava unique, ja INSERTIN sijaan INSERT OR UPDATE
    def add_result(self, person_id, task_id, result):
        """lisää tieokantatauluun uuden tuloksen
        Args:   person_id: henkilön pk id
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
        cursor = self._con.cursor()
        sql = """DELETE FROM Results"""
        cursor.execute(sql)
        self._con.commit()


# tämä luokka ei ole valmis, tarvitaan lisää hakutoimintoja
resultrepository = ResultRepository()
