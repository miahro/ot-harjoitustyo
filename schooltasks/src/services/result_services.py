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
        # print(type(person_id))
        # print(type(task_id))
        # print(type(result))
        resultrepository.add_result(person_id, task_id, result)
#        resultrepository.add_result(1, 1, False)
#        resultrepository.add_result(person_id, task_id, result)


    def user_totals(self, user_id):
        person_id = userrepository.get_pk_id(user_id)[0]
        correct = resultrepository.get_user_total_correct(person_id)[0]
        fail = resultrepository.get_user_total_fail(person_id)[0]
        return {"correct": correct, "fail": fail, "total_tasks": correct+fail,
                "correct_percent": round(100*correct/(correct+fail), 1)}


resultservices = ResultServices()
