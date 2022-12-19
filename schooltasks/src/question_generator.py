"""sisältää luokan QuestionGenerator"""
from random import choice, sample
import csv
from config import TASKS_INPUT_PATH, DIFFICULTY_RANGE


class QuestionGenerator:
    """Luokka kysymysten automaattista luontia varten"""

    def __init__(self):
        self.filepath = TASKS_INPUT_PATH

    def addition(self):
        """luo yhteenlaskukysymykset"""
        std_part = "Valitse seuraavan yhteenlaskun oikea tulos: "
        task_list = []
        for difficulty in DIFFICULTY_RANGE:
            for _ in range(1, 10*difficulty+1):
                task = {}
                task["topic"] = 1
                task["difficulty"] = difficulty
                selection = list(range(1, 10*difficulty))
                off_range = [-2, -1, 1, 2]
                operand1 = choice(selection)
                operand2 = choice(selection)
                task["question"] = std_part + \
                    "".join([str(operand1), " + ", str(operand2), " = "])
                cor_num = operand1+operand2
                wrong_num = sample(off_range, 3)
                task["correct"] = "".join(str(cor_num))
                task["wrong1"] = "".join(str(wrong_num[0]+cor_num))
                task["wrong2"] = "".join(str(wrong_num[1]+cor_num))
                task["wrong3"] = "".join(str(wrong_num[2]+cor_num))
                task_list.append(task)
        self.write_csv(task_list)

    def subtraction(self):
        """"luo vähennyslaskukysymykset"""
        std_part = "Valitse seuraavan vähennyslaskun oikea tulos: "
        task_list = []
        for difficulty in DIFFICULTY_RANGE:
            for _ in range(1, 10*difficulty+1):
                task = {}
                task["topic"] = 2
                task["difficulty"] = difficulty
                selection = list(range(1, 10*difficulty))
                off_range = [1, 2, 3, 4]
                operand1 = choice(selection)
                operand2 = choice(selection)
                if difficulty < 5 and operand1 < operand2:
                    operand1, operand2 = operand2, operand1
                task["question"] = std_part + \
                    "".join([str(operand1), " - ", str(operand2), " = "])
                cor_num = operand1-operand2
                wrong1_num, wrong2_num, wrong3_num = sample(off_range, 3)
                task["correct"] = "".join(str(cor_num))
                task["wrong1"] = "".join(str(wrong1_num+cor_num))
                task["wrong2"] = "".join(str(wrong2_num+cor_num))
                task["wrong3"] = "".join(str(wrong3_num+cor_num))
                task_list.append(task)
        self.write_csv(task_list)

    def multiplication(self):
        """luo kertolaskukysymykset"""
        std_part = "Valitse seuraavan kertolaskun oikea tulos: "
        task_list = []
        for difficulty in DIFFICULTY_RANGE:
            for _ in range(1, 10*difficulty+1):
                task = {}
                task["topic"] = 3
                task["difficulty"] = difficulty
                selection = list(range(1, 10*difficulty))
                off_range = [-2, -1, 1, 2]
                operand1 = choice(selection)
                operand2 = choice(selection)
                task["question"] = std_part + \
                    "".join([str(operand1), " * ", str(operand2), " = "])
                cor_num = operand1*operand2
                wrong1_num, wrong2_num, wrong3_num = sample(off_range, 3)
                task["correct"] = "".join(str(cor_num))
                task["wrong1"] = "".join(str(wrong1_num+cor_num))
                task["wrong2"] = "".join(str(wrong2_num+cor_num))
                task["wrong3"] = "".join(str(wrong3_num+cor_num))

                task_list.append(task)
        self.write_csv(task_list)

    def division(self):
        """luo jakolasku kysymykset"""
        std_part = "Valitse seuraavan jakolaskun oikea tulos: "
        task_list = []
        for difficulty in DIFFICULTY_RANGE:
            for _ in range(1, 10*difficulty+1):
                task = {}
                task["topic"] = 4
                task["difficulty"] = difficulty
                selection = list(range(1, 10*difficulty))
                off_range = list(range(10))
                operand1 = choice(selection)
                operand2 = choice(selection)
                task["question"] = std_part + \
                    "".join([str(operand1), " / ", str(operand2), " = "])
                cor_num = operand1//operand2, operand1 % operand2
                wr_div = sample(off_range, 3)
                wr_rem = sample(off_range, 3)
                task["correct"] = f"osamäärä = {str(cor_num[0])}, jakojäännös = {str(cor_num[1])}"
                task["wrong1"] = f"osamäärä = {str(wr_div[0])}, jakojäännös = {str(wr_rem[0])}"
                task["wrong2"] = f"osamäärä = {str(wr_div[1])}, jakojäännös = {str(wr_rem[1])}"
                task["wrong3"] = f"osamäärä = {str(wr_div[2])}, jakojäännös = {str(wr_rem[2])}"
                task_list.append(task)
        self.write_csv(task_list)

    def write_csv(self, task_list):
        """kirjoittaa kysymyslistan csv-kysymystiedoston riveiksi
        lisää vanhojen perään, ei ylikirjoita
        Args    task_list: kysymyslista, lista sanakirjoja
        """
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['topic', 'difficulty', 'question',
                          'correct', 'wrong1', 'wrong2', 'wrong3']
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerows(task_list)

    def write_csv_headers(self):
        """kirjoittaa otsikkotiedot kysymystiedostoon
        huom! korvaa mahdollisen edellisen samannimisen tiedoston"""
        with open(self.filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['topic', 'difficulty', 'question',
                          'correct', 'wrong1', 'wrong2', 'wrong3']
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

    def populate_csv(self):
        """kutsuu ensin kysymystiedoston otsikkojen luontia, ja
        tämän jälkeen yksittäisten kysymyssarjojen luontifunktioita"""
        self.write_csv_headers()
        self.addition()
        self.subtraction()
        self.multiplication()
        self.division()


def generate():
    """pääohjelma, luo QuestionGenerator olion
    ja kutsuu kysymysten luontifunktiota populate_csv()"""
    question_generator = QuestionGenerator()
    question_generator.populate_csv()


if __name__ == "__main__":
    generate()

questiongenerator = QuestionGenerator()