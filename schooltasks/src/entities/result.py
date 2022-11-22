"""moduli sisältää result -luokan eli tuloksen"""

class Result:
    """luokka tuloksen ominaisuuksille"""
    def __init__(self, person, task, result):
        """alustaa Result luokan olion
        Args:   person: henkilö, User luokan olio
                task: tehtävä, Task luokan olio
                result: tulos boolean """
        self.person = person
        self.task = task
        self.result = result
    
                