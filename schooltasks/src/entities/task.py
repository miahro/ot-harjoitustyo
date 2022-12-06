"""moduli sisältää task eli tehtävä-luokan"""


class Task:
    """luokka tehtävävän ominaisuuksille
    Attributes:
        topic_id: aihetunniste Topic luokasta
        difficulty: vaikeustaso, kokonaisluku
        question: kysymys, merkkijono
        correct: oikea vastausvaihtoehto, merkkijono
        wrong1-3: väärät vastausvaihtoehdot, merkkijonoja
        task_id: tehtävän pkid tietokantataulussa"""

    def __init__(self, task_dict):
        """alustaa Task luokan olion
        Args:   task_dict
                task_dict, keys/values
                    topic_id: aihetunniste Topic luokasta
                    difficulty: vaikeustaso, kokonaisluku
                    question: kysymys, merkkijono
                    correct: oikea vastausvaihtoehto, merkkijono
                    wrong1-3: väärät vastausvaihtoehdot, merkkijonoja
                    task_id: tehtävän pkid tietokantataulussa"""
        self.topic_id = task_dict["topic_id"]
        self.difficulty = task_dict["difficulty"]
        self.question = task_dict["question"]
        self.correct = task_dict["correct"]
        self.wrong1 = task_dict["wrong1"]
        self.wrong2 = task_dict["wrong2"]
        self.wrong3 = task_dict["wrong3"]
        self.task_id = task_dict["task_id"]
        # tietokannan pkid:n pitäminen luokan
        # entities luokan muuttujana on kyseenalaista
        # mutta tässä tapauksessa turvallisinta

    def __repr__(self):
        return f"Task({self.topic_id}, {self.difficulty}, {self.question}, "\
            f"{self.correct}, {self.wrong1}, {self.wrong2}, {self.wrong3}"

    def __str__(self):
        return f"topic_id: {self.topic_id}, difficulty: {self.difficulty}, "\
            f"question: {self.question}, correct: {self.correct}, "\
            f"wrong1: {self.wrong1}, wrong2: {self.wrong2}, wrong3: {self.wrong3}"
