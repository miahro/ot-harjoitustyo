"""moduli sisältää luokan TaskView"""
import random
from tkinter import ttk, constants, IntVar
from services.user_services import userservices
from services.task_services import taskservices
from services.topic_services import topicservices
from services.result_services import resultservices


class TaskView:
    """Luokka tehtävien tekemisnäyttöä varten
    Attributes:
        root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
        handle_choice: metodikahva valintänäkymälle
        frame: TK-Inter Frame-widget
        task_list: taskservices olion palauttama 10:n tehtävän sarja
        correct: oikeat vastaukset kierroksella, tämä vaina paikalista näyttöä varten
        wrong: väärät vastaukset kierroksella, tämä vaina paikalista näyttöä varten

    """

    def __init__(self, root, handle_choice):
        """Luokan konstruktori

        Args:
            root: pääohjelman TK-inter -elementti, johon näkymä alustetaan
            handle_choice: metodikahva valintänäkymälle
        """
        self._root = root
        self._handle_choice = handle_choice
        self._frame = None
        self._task_list = taskservices.get_tasks(
            topicservices.active_topic, taskservices.active_difficulty, 10)
        # tämä vain tulosten väliaikaiseta / paikallista näyttöä varten tehtävävänäkymässä
        self._correct = 0
        # tämä vain tulosten väliaikaiseta / paikallista näyttöä varten tehtävävänäkymässä
        self._wrong = 0

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _answer(self, value, task_id):
        """Kutsuu sovelluslogiikan tulosten päivitysmetodia

        Args:
            value: vastauksen arvo, 1 jos oikein, muuten negatiivinen
            task_id: tehtävän tunniste
        """
        if value <= 0:
            self._wrong += 1
            resultservices.add_result(userservices.active_user_details()[
                                      'user_id'], task_id, False)
        else:
            self._correct += 1
            resultservices.add_result(userservices.active_user_details()[
                                      'user_id'], task_id, True)
        self.destroy()
        self._initialize()

    def _initialize(self):
        """Alustaa näkymän"""
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tehtävien tekeminen", font=(
            'Helvetica', 12, 'bold'))
        label.grid(padx=5, pady=5, sticky=constants.EW)

        user_label = ttk.Label(
            master=self._frame, text=f"Kirjautunut käyttäjä: {userservices.active_user_details()['user_id']}")
        user_label.grid(padx=5, pady=5, sticky=constants.EW)

        topic_label = ttk.Label(
            master=self._frame, text=f"Valittu aihe: {topicservices.return_active_topic()}")
        topic_label.grid(padx=5, pady=5, sticky=constants.EW)

        difficulty_label = ttk.Label(
            master=self._frame, text=f"Valittu vaikeustaso: {taskservices.return_active_difficulty_str()}")
        difficulty_label.grid(padx=5, pady=5, sticky=constants.EW)

        task_label = ttk.Label(
            master=self._frame, text=f"Tehtävä", font=('Helvetica', 12, 'bold'))
        task_label.grid(padx=5, pady=5, sticky=constants.EW)

        if len(self._task_list) > 0:
            task = self._task_list.pop()
            question_label = ttk.Label(
                master=self._frame, text=f"{task.question}")
            question_label.grid(padx=5, pady=5, sticky=constants.EW)

            def get_choice():
                value = choice.get()
                self._answer(value, task.task_id)

            answer_options = [(task.correct, 1), (task.wrong1, -1),
                              (task.wrong2, -2), (task.wrong3, -3)]
            random.shuffle(answer_options)
            choice = IntVar()
            for option in answer_options:
                r = ttk.Radiobutton(
                    master=self._frame,
                    text=option[0],
                    value=option[1],
                    variable=choice,
                )
                r.grid(padx=5, pady=5, sticky=constants.EW)

            next_button = ttk.Button(
                master=self._frame,
                text="Vastaa",
                command=get_choice
            )
            next_button.grid(padx=5, pady=5, sticky=constants.EW)

        else:
            end_label = ttk.Label(
                master=self._frame, text=f"Kaikkiin tehtäviin vastattu. Oikeita vastauksia {self._correct}, vääriä vastauksia {self._wrong}")
            end_label.grid(padx=5, pady=5, sticky=constants.EW)

            button = ttk.Button(
                master=self._frame,
                text="Palaa takaisin",
                command=self._handle_choice
            )
            button.grid(padx=5, pady=5, sticky=constants.EW)

        self.pack()
