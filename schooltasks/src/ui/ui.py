from tkinter import Tk
from ui.start_view import StartView
from ui.login_view import LoginView
from ui.new_user_view import NewUserView
from ui.choice_view import ChoiceView
from ui.task_view import TaskView
from ui.results_view import ResultView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login(self):
        self._show_login_view()

    def _handle_start(self):
        print("ui _handle_start")
        self._show_start_view()

    def _handle_new_user(self):
        self._show_new_user_view()

    def _handle_choice(self):
        print("ui _handle_choice")
        self._show_choice_view()

    def _handle_task(self):
        self._show_task_view()

    def _handle_result(self):
        self._show_result_view()

    def _show_result_view(self):
        self._hide_current_view()
        self._current_view = ResultView(
            self._root,
            self._handle_start,
            self._handle_choice
        )

    def _show_task_view(self):
        self._hide_current_view()
        self._current_view = TaskView(
            self._root,
            self._handle_start,
            self._handle_choice
        )

    def _show_choice_view(self):
        self._hide_current_view()
        self._current_view = ChoiceView(
            self._root,
            self._handle_start,
            self._handle_task,
            self._handle_result
        )

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_login,
            self._handle_new_user
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_start,
            self._handle_choice,
            self._show_choice_view
        )

        self._current_view.pack()

    def _show_new_user_view(self):
        self._hide_current_view()

        self._current_view = NewUserView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()
