"""sisältää luoka TopicServices"""

from repositories.topic_repository import topicrepository
#from repositories.task_repository import TaskRepository
#from repositories.user_repository import userrepository


class TopicServices:
    """luokka aiheiden palveluita varten"""

    def __init__(self):
        """konstruktori alustaaa tyhjän olion ja käyttää taskrepository oliota"""
        self.topicrepository = topicrepository
        self.active_topic = None
        # self.min_difficulty = topicrepository.min_difficulty()
        # self.max_difficulty = topicrepository.max_difficulty()

    def update_topics_db(self):
        """lukee tehtävät cvs-tiedostosta ja päivittää tietokannan tehtävät"""
        topic_list_from_file = self.topicrepository.read_from_file()
        self.topicrepository.update_db(topic_list_from_file)

    def get_all_topics(self):
        """palauttaa kaikki aihee string-listana"""
        return topicrepository.all_topics()

    def set_active_topic(self, topic):
        """asettaa valitun aiheen"""
        tid = self.topicrepository.id_by_topic(topic)
        self.active_topic = tid

    def return_active_topic(self):
        """palauttaa valitun aiheen
        jos aihetta ei valittu, palauttaa 'ei valittu'-viestin"""
        if self.active_topic is None:
            return "aihetta ei valittu"
        return self.topicrepository.topic_by_id(self.active_topic)


topicservices = TopicServices()
