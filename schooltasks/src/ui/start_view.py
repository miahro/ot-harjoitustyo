"""sisältää luokan StartView"""

from tkinter import ttk, constants


class StartView:
    """Alkunäkymä

    Attributes:
        root: pääohjelman TK-inter -elementti, johon näkymä alustetaa
        handle_login: metodikahva sisäänkirjautumisnäkymälle
        handle_new_user: metodikahva uuden käyttäjän luontinäkymälle
        frame: TK-Inter Frame-widget

    """

    def __init__(self, root, handle_login, handle_new_user):
        """Luokan konstruktori

        Args:
            root: pääohjelman TK-inter -elementti, johon näkymä alustetaa
            handle_login: metodikahva sisäänkirjautumisnäkymälle
            handle_new_user: metodikahva uuden käyttäjän luontinäkymälle
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_new_user = handle_new_user
        self._frame = None

        self._initialize()

    def pack(self):
        """näyttää näkymänt"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa näkymän"""
        self._frame.destroy()

    def _initialize(self):
        """alustaa näkymän"""
        self._frame = ttk.Frame(master=self._root)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login
        )

        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        new_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._handle_new_user
        )
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)
