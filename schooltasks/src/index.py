"""moduli sisältää pääohjelman"""
# import config
# from entities.user import User
# from repositories.user_repository import UserRepository
# from repositories.topic_repository import TopicRepository
# from repositories.task_repository import TaskRepository
# from repositories.result_repository import ResultRepository
# from entities.topic import Topic
from tkinter import Tk
from ui.ui import UI

# from dbcon import connection


def main():
    """pääohjelma, käynnistää käyttöliittymän"""

    window = Tk()
   # window.geometry("500x200")
    window.title("Matematiikan harjoittelusovellus")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
