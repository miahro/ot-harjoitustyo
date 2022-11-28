
"""moduli mahdollistaa tietokannan luonnin komentoriviltä"""
from dbinit import init_db


def build():
    """kutsuu vain dbinit.init_db()-funktiota"""
    init_db()


if __name__ == "__main__":
    build()
