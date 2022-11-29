from tkinter import ttk, constants
from services.user_services import userservices


class ChoiceView:
    def __init__(self, root, handle_start, handle_task, handle_result, show_start_view):
        self._root = root
        self._handle_start = handle_start
        self._handle_task = handle_task
        self._handle_result = handle_result
        self._show_start_view = show_start_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout(self):
        userservices.logout()
        print(userservices.logged_in_user)
        self._show_start_view()        

    def _initialize(self):
        print(userservices.logged_in_user)
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Valintanäkymä")
        label.grid(row=5, column=0)

        user_label = ttk.Label(master=self._frame, text=f"Kirjautunut käyttäjä: {userservices.active_user_details()['user_id']}")
        user_label.grid(row=6, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout
            #command=self._handle_start
        )
        button.grid(row=8, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Tee tehtäviä",
            command=self._handle_task
        )
        button.grid(row=12, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Näytä tulokset",
            command=self._handle_result
        )
        button.grid(row=15, column=0)

        self.pack()
