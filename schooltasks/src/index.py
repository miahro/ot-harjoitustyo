"""moduli sisältää pääohjelman"""
from tkinter import Tk
from ui.ui import UI


def main():
    """pääohjelma, käynnistää käyttöliittymän"""

    window = Tk()
    window.geometry("1300x1000")
    window.title("Matematiikan harjoittelusovellus")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
