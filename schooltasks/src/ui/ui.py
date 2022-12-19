"""moduli sisältää luokan UI"""
from tkinter import Tk
from ui.start_view import StartView
from ui.login_view import LoginView
from ui.new_user_view import NewUserView
from ui.choice_view import ChoiceView
from ui.task_view import TaskView
from ui.results_view import ResultView


class UI:
    """Luokka sovelluksen käyttöliittymää varten

    Attributes:
        root: pääohjelman TK-Inter elementti, johon näkymä alustetaan
    """

    def __init__(self, root):
        """Luokan konstruktori

        Args:
            root: pääohjelman TK-Inter elementti, johon näkymä alustetaan
        """
        self._root = root
        self._current_view = None

    def start(self):
        """määrittää aloitusnäkymän"""
        self._show_start_view()

    def _hide_current_view(self):
        """piilottaa nykyisen näkymän"""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login(self):
        """metodikahva kirjautumisnäkymälle"""
        self._show_login_view()

    def _handle_start(self):
        """metodikahva aloitusnäkymälle"""
        self._show_start_view()

    def _handle_new_user(self):
        """metodikahva uuden käyttäjän luonti näkymälle"""
        self._show_new_user_view()

    def _handle_choice(self):
        """metodikahva valintanäkymälle"""
        self._show_choice_view()

    def _handle_task(self):
        """metodikahva tehtävänäkymälle"""
        self._show_task_view()

    def _handle_result(self):
        """metodikahva tulosnäkymälle"""
        self._show_result_view()

    def _show_result_view(self):
        """alustaa ResultView-olion, asettaa sen näkymäksi
        ja näyttää näkymän"""
        self._hide_current_view()
        self._current_view = ResultView(
            self._root,
            self._handle_choice
        )

    def _show_task_view(self):
        """alustaa TaskView-olion, asettaa sen näkymäksi
        ja näyttää näkymän"""
        self._hide_current_view()
        self._current_view = TaskView(
            self._root,
            self._handle_choice
        )

    def _show_choice_view(self):
        """alustaa ChoiceView-olion, asettaa sen näkymäksi
        ja näyttää näkymän"""
        self._hide_current_view()
        self._current_view = ChoiceView(
            self._root,
            self._handle_task,
            self._handle_result,
            self._show_start_view
        )

    def _show_start_view(self):
        """alustaa StartView-olion, asettaa sen näkymäksi
        ja näyttää näkymän"""
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_login,
            self._handle_new_user
        )

        self._current_view.pack()

    def _show_login_view(self):
        """alustaa LoginView-olion, asettaa sen 
        näkymäksi ja näyttää näkymän"""
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_choice_view,
            self._show_start_view
        )

        self._current_view.pack()

    def _show_new_user_view(self):
        """alustaa NewUserView-olion näkymäksi
        ja näyttää näkymän"""
        self._hide_current_view()

        self._current_view = NewUserView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()
