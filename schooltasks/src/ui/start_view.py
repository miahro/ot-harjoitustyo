from tkinter import ttk, constants


class StartView:
    def __init__(self, root, handle_login, handle_new_user):
        self._root = root
        self._handle_login = handle_login
        self._handle_new_user = handle_new_user
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # label = ttk.Label(master=self._frame, text="Start view")
        # label.grid(row=0, column=0)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login
        )

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        #login_button.grid(row=4, column=0)

        new_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._handle_new_user
        )
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        #button.grid(row=6, column=0)
