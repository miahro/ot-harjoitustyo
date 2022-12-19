
"""sisältää luokan ResultView"""
from tkinter import ttk, constants, Text, Entry
from services.user_services import userservices
from services.result_services import resultservices
from ui.plot_details import plot_user_details


class ResultView:
    """Näkymä tulosten näyttämiseksi
    Attributes:
            root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
            handle_choice: metodikahva valintanäkymälle

    """

    def __init__(self, root, handle_choice):
        """Luokan konstruktori

        Args:
            root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
            handle_choice: metodikahva valintanäkymälle
        """
        self._root = root
        self._handle_choice = handle_choice
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _totals(self):
        """Kutsuu sovelluslogiikan tulosten palatusmetodeja
        sekä aktiivisen käyttäjän tiet palauttavaa metodia
        ja näyttää tulokset 
        """
        totals = resultservices.user_totals(
            userservices.active_user_details()['user_id'])
        by_topic = resultservices.user_results_by_topic_all_topics(
            userservices.active_user_details()['user_id']
        )
        user_label = ttk.Label(
            master=self._frame, text=f"Oppilaan {userservices.active_user_details()['first_name']} {userservices.active_user_details()['last_name']} tulokset: "
        )
        user_label.grid(padx=5, pady=5, sticky=constants.EW)

        columns = ("difficulty", "total", "correct", "fail", "correct_percent")

        tree = ttk.Treeview(master=self._frame, columns=columns, height=7)
        tree.grid(padx=5, pady=5)

        tree.heading('#0', text='Aihe')
        tree.heading('difficulty', text='Vaikeustaso')
        tree.heading('total', text='Yhteensä')
        tree.heading('correct', text='Oikein')
        tree.heading('fail', text='Väärin')
        tree.heading('correct_percent', text='Oikein-%')

        tree.insert('', 'end', iid=0, text="kaikki aiheet", values=(f"kaikki vaikeustasot", f"{totals['total_tasks']}",
                    f"{totals['correct']}", f"{totals['fail']}", f"{totals['correct_percent']} %"))
        for idx, topic in enumerate(by_topic):
            tree.insert('', 'end', iid=idx+1, text=f"{topic['topic']}", values=(f"kaikki vaikeustasot", f"{topic['total_tasks']}",
                                                                                f"{topic['correct']}", f"{topic['fail']}", f"{topic['correct_percent']} %"))

    def _plot_details(self):
        """Näyttää aktiivisen käyttäjän tulokset
        erillisessä ikkunassa"""
        user=userservices.active_user_details()
        details=resultservices.user_details(user_id=user['user_id'])
        plot_user_details(user=user, details=details)

    def _initialize(self):
        """Alustaa näkymän"""
        self._frame = ttk.Frame(master=self._root)

        result_label = ttk.Label(
            master=self._frame, text=f"Tulokset", font=('Helvetica', 12, 'bold'))
        result_label.grid(padx=5, pady=5, sticky=constants.EW)

        self._totals()


        details_button = ttk.Button(
            master=self._frame,
            text="Näytä tulosten yksityiskohdat",
            command=self._plot_details
        )
        details_button.grid(padx=5, pady=5, sticky=constants.EW)



        back_button = ttk.Button(
            master=self._frame,
            text="Palaa takaisin",
            command=self._handle_choice
        )
        back_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.pack()
