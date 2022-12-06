"""moduli sisältää Result -luokan eli tuloksen"""


class Result:
    """luokka tuloksen ominaisuuksille
    Attributes:
        person: henkilö, Person-luokan olio
        task: tehtävä, Task-luokan olio
        Result: tulos, boolean """

    def __init__(self, person, task, result):
        """alustaa Result luokan olion
        Args:   person: henkilö, User luokan olio
                task: tehtävä, Task luokan olio
                result: tulos boolean """
        self.person = person
        self.task = task
        self.result = result

    def __repr__(self):
        return f"Result({self.person.__repr__()}, {self.task.__repr__()}, {self.result.__repr__()})"

    def __str__(self):
        return f"{self.person.__str__()}, {self.task.__str__()}, {self.result.__str__()}"
