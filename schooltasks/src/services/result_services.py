"""sisältää luokan ResultServices"""

from repositories.result_repository import resultrepository
from repositories.user_repository import userrepository
from repositories.topic_repository import topicrepository


class ResultServices:
    """luokka tulosten palveluille"""

    def __init__(self):
        self.resultrepository = resultrepository

    def add_result(self, user_id, task_id, result):
        """lisää uuden tulosrivin käyttäjälle
        Args:
            user_id: käyttäjätunnus
            task_id: tehtävän pkid
            result: boolean (oikein, väärin) """
        person_id = userrepository.get_pk_id(
            user_id)[0]  # vaatii poikkeuskäsittelyn
        resultrepository.add_result(person_id, task_id, result)

    def user_totals(self, user_id):
        """hakee käyttäjän tulosten kokonaisuuden
        Args:
            user_id: käyttäjätunnus
        Returns:
            tulosten yhteenveto sanakirjana
        """
        person_id = userrepository.get_pk_id(
            user_id)[0]  # vaatii poikkeuskäsittelyn
        correct = resultrepository.get_user_total_correct(person_id)[0]
        fail = resultrepository.get_user_total_fail(person_id)[0]
        return {"correct": correct, "fail": fail, "total_tasks": correct+fail,
                "correct_percent": 0.0
                if correct+fail == 0
                else round(100*correct/(correct+fail), 1)}

    def user_results_by_topic(self, user_id, topic):
        """hakee käyttäjän tulokset annetusta aiheesta
        Args:
            user_id: käyttäjätunnus
            topic: aihe
        Returns:
            Tulokset sanakirjana
        """
        person_id = userrepository.get_pk_id(
            user_id)[0]  # vaatii poikkeuskäsittelyn
        topic_id = topicrepository.id_by_topic(topic)
        correct = resultrepository.get_user_correct_by_topic(person_id, topic_id)[
            0][0]
        fail = resultrepository.get_user_false_by_topic(person_id, topic_id)[
            0][0]
        return {"topic": topic, "correct": correct, "fail": fail, "total_tasks": correct+fail,
                "correct_percent": 0.0
                if correct+fail == 0
                else round(100*correct/(correct+fail), 1)}


    def user_results_by_topic_all_topics(self, user_id):
        """"hakee käyttäjän tulokset kaikista aiheista
        aiheen mukaan lajiteltuna
        Args:
            user_id: käyttäjätunnus
        Returns:
            lista tuloksissa, lista sanakirjoja per aihe
        """
        topics = topicrepository.all_topics()
        result_by_topic = []
        for topic in topics:
            result_by_topic.append(self.user_results_by_topic(user_id, topic))
        return result_by_topic

#tämä metodi on kesken, ei toimi kunnolla, eikä tätä vielä käytä mikään muu sovelluksen osa,
# joten kommentoitu pois. Tarvitaan ja korjataan loppupalautukseen

    # def user_details(self, user_id):
    #     """hakee käyttäjän tulosten yksityiskohdat
    #     Args:
    #         user_id: käyttäjätunnus
    #     Returns:
    #         EI VIELÄ MITÄÄN, TÄMÄ ON KESKEN"""
    #     person_id = userrepository.get_pk_id(user_id)[0]
    #     correct = resultrepository.get_user_all_correct(person_id)
    #     fail = resultrepository.get_user_all_false(person_id)
    #     all_topics = topicrepository.all_topics()
    #     all = {}
    #     all = all.fromkeys(all_topics, )
    #     for topic in all.keys():
    #         topic_id = topicrepository.id_by_topic(topic)
    #         lst = []
    #         print(f"topic_id {topic_id}")
    #         lst = [list(item) for item in (
    #             resultrepository.get_user_details_by_topic(person_id, topic_id))]
    #         all[topic] = lst
    #     lst = [list(ele) for ele in all]
    #     return all

    def delete_all(self):
        """tyhjentää tietokannan Results taulun"""
        self.resultrepository.delete_all()


resultservices = ResultServices()
