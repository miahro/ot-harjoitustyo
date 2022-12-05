"""sisältää luoka TaskServices"""

from repositories.task_repository import taskrepository
#from repositories.task_repository import TaskRepository
#from repositories.user_repository import userrepository


class TaskServices:
    """luokka tehtävien palveluita varten"""

    def __init__(self):
        """konstruktori alustaaa tyhjän olion ja käyttää taskrepository oliota"""
        self.taskrepository = taskrepository
        self.active_difficulty = None

    def update_tasks_db(self):
        """lukee tehtävät cvs-tiedostosta ja päivittää tietokannan tehtävät"""
        task_list_from_file = self.taskrepository.read_from_file()
        self.taskrepository.update_db(task_list_from_file)


    def get_tasks(self, topic_id, difficulty, pcs):
        """palauttaa joukon saunnaisia tehtäviä
        Args    topic_id: aihetunniste
                difficulty: vaikeustaso
                pcs: palautettavien tehvätien määrä"""
        result = taskrepository.get_random_task_list(
            topic_id=topic_id, difficulty=difficulty, tasks_no=pcs)
        return result

    def return_min_difficulty(self):
        """funktio palauttaa minimivaikeustason"""
        return self.taskrepository.min_difficulty()

    def return_max_difficulty(self):
        """funktio palauttaa maksimivaikeustason"""
        return self.taskrepository.max_difficulty()

    def return_difficulty_range(self):
        """funktio palauttaa listana vaikeustasot [minimi,...,maksimi]"""
        return list(range(self.return_min_difficulty(), self.return_max_difficulty()+1))

    def return_active_difficulty_str(self):
        """palauttaa valitun vaikeuson
        palautus stringinä. Jos ei valittua vaikeustasoa palauttaa
        viestin 'ei valittu'"""
        if self.active_difficulty is None:
            return "vaikeustasoa ei valittu"
        return str(self.active_difficulty)

    def set_active_difficulty(self, difficulty):
        """asetttaaa valitun vaikeustason"""
        self.active_difficulty = int(difficulty)


taskservices = TaskServices()
