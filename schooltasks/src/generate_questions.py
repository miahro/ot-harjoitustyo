
"""moduli mahdollistaa kysymys csv-tiedoston luonnin komentorirviltä"""
from question_generator import generate


def generate_questions():
    """kutsuu vain dbinit.init_db()-funktiota"""
    generate()


if __name__ == "__main__":
    generate_questions()
