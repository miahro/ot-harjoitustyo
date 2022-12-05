"""moduli sisältää task eli tehtävä-luokan"""


class Task:
    """luokka tehtävävän ominaisuuksille"""

    # def __init__(self, topic_id, difficulty, question, correct, wrong1, wrong2, wrong3):
    #     """alustaa Task luokan olion
    #     Args:   topic_id: aihetunniste Topic luokasta
    #             difficulty: vaikeustaso, kokonaisluku
    #             question: kysymys, merkkijono
    #             correct: oikea vastausvaihtoehto, merkkijono
    #             wrong1-3: väärät vastausvaihtoehdot, merkkijonoja"""
    #     self.topic_id = topic_id
    #     self.difficulty = difficulty
    #     self.question = question
    #     self.correct = correct
    #     self.wrong1 = wrong1
    #     self.wrong2 = wrong2
    #     self.wrong3 = wrong3

    def __init__(self, task_dict):
        """alustaa Task luokan olion
        Args:   topic_id: aihetunniste Topic luokasta
                difficulty: vaikeustaso, kokonaisluku
                question: kysymys, merkkijono
                correct: oikea vastausvaihtoehto, merkkijono
                wrong1-3: väärät vastausvaihtoehdot, merkkijonoja"""
        self.topic_id = task_dict["topic_id"]
        self.difficulty = task_dict["difficulty"]
        self.question = task_dict["question"]
        self.correct = task_dict["correct"]
        self.wrong1 = task_dict["wrong1"]
        self.wrong2 = task_dict["wrong2"]
        self.wrong3 = task_dict["wrong3"]

    def __str__(self):
        task = f"topic_id: {self.topic_id}, difficulty: {self.difficulty}, question: {self.question}, correct: {self.correct}, wrong1: {self.wrong1}, wrong2: {self.wrong2}, wrong3: {self.wrong3}"
        return task
