"""Sisältää luokan LoginView"""
from tkinter import ttk, constants, StringVar
from ui.choice_view import ChoiceView
from services.user_services import userservices


class LoginView:
    """Luokka sisäänkirjautumisnäkymää varten
    Attributes:
        root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
        handle_start: metodikahva alkunäkymälle
        show_choice_view: viittaus valintanäkymään
        show_start_view: viittaus aloitusnäkymään
        self._frame: TK-Inter widget

    """

    def __init__(self, root, show_choice_view, show_start_view):
        """Luokan konstruktori

        Args:
            root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
            handle_start: metodikahva alkunäkymälle
            show_start_view: viittaus aloitusnäkymään
            show_start_view: viittaus aloitusnäkymään
            self._frame: TK-Inter widget
        """
        self._root = root
        self._show_choice_view = show_choice_view
        self._show_start_view = show_start_view
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _login(self):
        """Lukee sisäänkirjautumistiedot ja kutsuu sovelluslogiikan sisäänkirjautumismetodia
        siirtyy valintanäkymään jos kirjautuminen onnistui
        näyttää virheviestin, jos kirjautumminen ei onnistunut"""
        user_id = self._user_id_entry.get()
        passwd = self._passwd_entry.get()

        result = userservices.login(user_id, passwd)
        if result[0]:
            self._show_choice_view()
        else:
            self._show_message(result[1])
            self._clear_entry_fields()

    def _clear_entry_fields(self):
        """tyhjentää sisäänkirjautumiskentät"""
        self._user_id_entry.delete(0, 'end')
        self._passwd_entry.delete(0, 'end')

    def _initialize_input_fields(self):
        """alustaa sisäänkirjautumiskentät"""

        user_id_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._user_id_entry = ttk.Entry(master=self._frame)
        user_id_label.grid(padx=5, pady=5, sticky=constants.W)
        self._user_id_entry.grid(padx=5, pady=5, sticky=constants.EW)

        passwd_label = ttk.Label(master=self._frame, text="Salasana")
        self._passwd_entry = ttk.Entry(master=self._frame)
        passwd_label.grid(padx=5, pady=5, sticky=constants.W)
        self._passwd_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _show_message(self, message):
        """näyttää virheviestin"""
        self._message.set(message)
        self._message_label.grid()

    def _initialize(self):
        """alustaa näkymän"""
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Sisään kirjautuminen")
        label.grid(row=0, column=0)

        self._message = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message,
            foreground='red'
        )
        self._message_label.grid(padx=5, pady=5)

        self._initialize_input_fields()

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        return_button = ttk.Button(
            master=self._frame,
            text="Palaa",
            command=self._show_start_view
        )
        return_button.grid(padx=5, pady=5, sticky=constants.EW)
