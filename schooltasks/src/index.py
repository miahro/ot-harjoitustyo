"""moduli sisältää pääohjelman"""
import sys
from tkinter import Tk
from dbcon import connection
from ui.ui import UI


def main():
    """pääohjelma, käynnistää käyttöliittymän"""

    window = Tk()
    window.geometry("1300x600")
    window.title("Matematiikan harjoittelusovellus")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    #komentoriviltä suoritettaessa tarkistetaan tietokannan taulujen
    #olemassaolo
    if not connection.execute(
        "SELECT COUNT(*) FROM sqlite_master\
        WHERE type='table' AND name='Results';").fetchone()[0] == 1 or\
    not connection.execute(
        "SELECT COUNT(*) FROM sqlite_master\
        WHERE type='table' AND name='Users';").fetchone()[0] == 1 or\
    not connection.execute(
        "SELECT COUNT(*) FROM sqlite_master\
        WHERE type='table' AND name='Topics';").fetchone()[0] == 1 or\
    not connection.execute(
        "SELECT COUNT(*) FROM sqlite_master\
        WHERE type='table' AND name='Tasks';").fetchone()[0] == 1:
        print("Database not initialized")
        print("Run build before starting program")
        sys.exit("DB not initialized")

    main()
