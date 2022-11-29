"""sisältää luoka TaskServices"""

from repositories.task_repository import taskrepository
#from repositories.task_repository import TaskRepository
#from repositories.user_repository import userrepository


class TaskServices:
    """luokka tehtävien palveluita varten"""

    def __init__(self):
        """konstruktori alustaaa tyhjän olion ja käyttää taskrepository oliota"""
        self.taskrepository = taskrepository

    def update_tasks_db(self):
        """lukee tehtävät cvs-tiedostosta ja päivittää tietokannan tehtävät"""
        task_list_from_file = self.taskrepository.read_from_file()
        self.taskrepository.update_db(task_list_from_file)
