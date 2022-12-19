"""sisältää luoka TaskServices"""

from repositories.task_repository import taskrepository


class TaskServices:
    """luokka tehtävien palveluita varten
    Attributes:
        taskrepository: tehtävä-repositorio -olio
        active_difficulty: valittu vaikeustaso"""

    def __init__(self):
        """konstruktori alustaaa tyhjän olion ja käyttää taskrepository oliota"""
        self.taskrepository = taskrepository
        self.active_difficulty = None

    def update_tasks_db(self):
        """lukee tehtävät cvs-tiedostosta ja päivittää tietokannan tehtävät"""
        task_list_from_file = self.taskrepository.read_from_file()
        self.taskrepository.update_db(task_list_from_file)

    def get_tasks(self, topic_id, difficulty, pcs):
        """hakee joukon saunnaisia tehtäviä
        Args
            topic_id: aihetunniste
            pcs: palautettavien tehvätien määrä
        Returns:
            lista tehtävä-olioita"""
        result = taskrepository.get_random_task_list(
            topic_id=topic_id, difficulty=difficulty, tasks_no=pcs)
        return result

    def return_min_difficulty(self):
        """hakee minimivaikeustason:
        Returns:
            minimivaikeustaso tietokannassa"""
        return self.taskrepository.min_difficulty()

    def return_max_difficulty(self):
        """hakee maksimivaikeustason
        Returns:
            maksimivaikeustaso tietokannassa"""
        return self.taskrepository.max_difficulty()

    def return_difficulty_range(self):
        """hakee vaikeustasojen alueen
        Returns:
            lista vaikeustasoja [min, ... , max]"""
        return list(range(self.return_min_difficulty(), self.return_max_difficulty()+1))

    def return_active_difficulty_str(self):
        """palauttaa valitun vaikeuson
        Returns: valittu vaikeustaso (str), jos ei valittua vaikeustasoa palauttaa
        viestin 'ei valittu'"""
        if self.active_difficulty is None:
            return "vaikeustasoa ei valittu"
        return str(self.active_difficulty)

    def set_active_difficulty(self, difficulty):
        """asetttaaa valitun vaikeustason
        Args:
            difficulty: vaikeustaso (int)"""
        self.active_difficulty = int(difficulty)


taskservices = TaskServices()
