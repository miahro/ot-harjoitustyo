"""konfigurointimoduuli asettaa tiedostopolut
tiedostojen nimet luetaan .env tiedostosta"""
import os
from dotenv import load_dotenv

directory = os.path.dirname(__file__)

load_dotenv(dotenv_path=os.path.join(directory, "..", ".env"))


TASKS_INPUT_FILENAME = os.getenv("TASKS_INPUT_FILE") or "task.csv"
TASKS_INPUT_PATH = os.path.join(directory, "..", "data", TASKS_INPUT_FILENAME)

TOPICS_INPUT_FILENAME = os.getenv("TOPICS_INPUT_FILE") or "topic.csv"
TOPICS_INPUT_PATH = os.path.join(
    directory, "..", "data", TOPICS_INPUT_FILENAME)

DB_FILE = os.getenv("DB_FILE") or "db.sqlite3"
DB_FILE_PATH = os.path.join(directory, "..", "data", DB_FILE)

TASK_KEYS = ("topic_id", "difficulty", "question",
             "correct", "wrong1", "wrong2", "wrong3", "task_id")

DIFFICULTY_RANGE = list(range(1, 11))
