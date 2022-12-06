"""sisältää luokan ResultServices"""

from repositories.result_repository import resultrepository
from repositories.user_repository import userrepository

class ResultServices:
    """luokka tulosten palveluille"""
    def __init__(self):
        self.resultrepository = resultrepository

    def add_result(self, user_id, task_id, result):
        """lisää uuden tulosrivin käyttäjälle
        Args    user_id: käyttäjätunnus
                task_id: tehtävän pkid
                result: boolean (oikein, väärin) """
        person_id = userrepository.get_pk_id(user_id)[0]
        resultrepository.add_result(person_id, task_id, result)

    def user_totals(self, user_id):
        person_id = userrepository.get_pk_id(user_id)[0]
        correct = resultrepository.get_user_total_correct(person_id)[0]
        fail = resultrepository.get_user_total_fail(person_id)[0]
        return {"correct": correct, "fail": fail, "total_tasks": correct+fail,
                "correct_percent": 0.0 if correct+fail==0 else round(100*correct/(correct+fail), 1)}

# tämä funktio on kesken, pitää tehdä jäkevä käsittely muotoon, joka voidaan palauttaa UI:lle näytettäväksi
    def user_details(self, user_id):
        person_id = userrepository.get_pk_id(user_id)[0]
        correct = resultrepository.get_user_all_correct(person_id)
        fail = resultrepository.get_user_all_false(person_id)
        print(correct)
        print(fail)


resultservices = ResultServices()
