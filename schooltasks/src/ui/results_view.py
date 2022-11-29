from tkinter import ttk, constants
from services.user_services import userservices

class ResultView:
    def __init__(self, root, handle_start, handle_choice):
        self._root = root
        self._handle_start = handle_start
        self._handle_choice = handle_choice
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tulosnäkymä")
        label.grid(row=4, column=0)

        user_label = ttk.Label(master=self._frame, text=f"Kirjautunut käyttäjä: {userservices.active_user_details()['user_id']}")
        user_label.grid(row=8, column=0)

        temp_label = ttk.Label(master=self._frame, text=f"Ei mitään järkevää vielä, tulokset tähän")
        temp_label.grid(row=10, column=0)


        # button = ttk.Button(
        #     master=self._frame,
        #     text="Palaa alkuun",
        #     command=self._handle_start
        # )



        # button.grid(row=10, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Palaa takaisin",
            command=self._handle_choice
        )
        button.grid(row=12, column=0)

        self.pack()
