"""moduuli tietokantayhteyttä varten"""
import sqlite3
from config import DB_FILE_PATH

connection = sqlite3.connect(DB_FILE_PATH)


def db_connection():
    """palauttaa sqlite3 tietokanta yhteyden
    tietokantatiedoston nimi määritelty .env tiedostossa"""
    return connection
