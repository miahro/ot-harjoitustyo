
"""moduli mahdollistaa tietokannan luonnin komentoriviltä"""
from os.path import isfile
from config import TASKS_INPUT_PATH
from dbinit import init_db


def build():
    """kutsuu vain dbinit.init_db()-funktiota"""
    if not isfile(TASKS_INPUT_PATH):
        print("Error: questions list missing")
        print("run poetry run invoke generate-questions or manually generate questions")
        exit()
    init_db()


if __name__ == "__main__":
    build()
