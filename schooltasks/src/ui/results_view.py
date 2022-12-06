from tkinter import ttk, constants, Text, Entry
from services.user_services import userservices
from services.result_services import resultservices


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

    def _totals(self):
        totals = resultservices.user_totals(
            userservices.active_user_details()['user_id'])
        user_label = ttk.Label(
            master=self._frame, text=f"Oppilaan {userservices.active_user_details()['first_name']} {userservices.active_user_details()['last_name']} tulokset: "
        )
        user_label.grid(padx=5, pady=5, sticky=constants.EW)
        # totals_label = ttk.Label(
        #     master=self._frame, text=f"Tehtäviä yhteensä: {totals['total_tasks']} \n"
        #     f"oikein: {totals['correct']}\n"
        #     f"väärin: {totals['fail']}\n"
        #     f"oikein prosentteina: {totals['correct_percent']}"
        # )
        # totals_label.grid(padx=5, pady=5, sticky=constants.EW)

        columns = ("difficulty", "total", "correct", "fail", "correct_percent")

        tree = ttk.Treeview(master=self._frame, columns=columns, height=20)
        tree.grid(padx=5, pady=5)

        tree.heading('#0', text='Aihe')
        tree.heading('difficulty', text='Vaikeustaso')
        tree.heading('total', text='Yhteensä')
        tree.heading('correct', text='Oikein')
        tree.heading('fail', text='Väärin')
        tree.heading('correct_percent', text='Oikein-%')

        tree.insert('', 'end', iid=0, text="kaikki aiheet", values=(f"kaikki vaikeustasot", f"{totals['total_tasks']}",
                    f"{totals['correct']}", f"{totals['fail']}", f"{totals['correct_percent']} %"))

    def _initialize(self):
        # self._frame = ttk.Frame(master=self._root)
        # label = ttk.Label(master=self._frame, text="Tulosnäkymä")
        # label.grid(padx=5, pady=5, sticky=constants.EW)

        # user_label = ttk.Label(
        #     master=self._frame, text=f"Kirjautunut käyttäjä: {userservices.active_user_details()['user_id']}")
        # user_label.grid(padx=5, pady=5, sticky=constants.EW)

        result_label = ttk.Label(
            master=self._frame, text=f"Tulokset", font=('Helvetica', 12, 'bold'))
        result_label.grid(padx=5, pady=5, sticky=constants.EW)

        self._totals()

        # tämä poistetaan kun näyttö on järkevä
        temp_label = ttk.Label(
            master=self._frame, text=f"Tämä on vasta alustava tulosnäyttö, parannetaan")
        temp_label.grid(padx=5, pady=5, sticky=constants.EW)

        button = ttk.Button(
            master=self._frame,
            text="Palaa takaisin",
            command=self._handle_choice
        )
        button.grid(padx=5, pady=5, sticky=constants.EW)

        self.pack()
