from tkinter import ttk, constants, OptionMenu, StringVar
from services.user_services import userservices
from services.topic_services import topicservices
from services.task_services import taskservices


class ChoiceView:
    def __init__(self, root, handle_start, handle_task, handle_result, show_start_view):
        self._root = root
        self._handle_start = handle_start
        self._handle_task = handle_task
        self._handle_result = handle_result
        self._show_start_view = show_start_view
#        self._choice_text = None
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout(self):
        userservices.logout()
        self._show_start_view()

    def _topic_choice(self, choice):
        topicservices.set_active_topic(choice)
       # print(choice)
        self.destroy()
        self._initialize()

    def _difficulty_choice(self, choice):
        taskservices.set_active_difficulty(choice)
        self.destroy()
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tehtävien valinta", font=(
            'Helvetica', 12, 'bold'))
        label.grid(padx=5, pady=5, sticky=constants.EW)

        user_label = ttk.Label(
            master=self._frame, text=f"Kirjautunut käyttäjä: {userservices.active_user_details()['user_id']}")
        user_label.grid(padx=5, pady=5, sticky=constants.EW)

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout
        )
        logout_button.grid(padx=5, pady=5, sticky=constants.EW)

# aiheen valinta
        top_choice_label = ttk.Label(
            master=self._frame, text="Valitse aihe", font=('Helvetica', 12, 'bold'))
        top_choice_label.grid(padx=5, pady=5, sticky=constants.EW)

        topic_label = ttk.Label(
            master=self._frame, text=f"Valittu aihe: {topicservices.return_active_topic()}")
        topic_label.grid(padx=5, pady=5, sticky=constants.EW)

        topics = topicservices.get_all_topics()
        topic_var = StringVar()
        topic_var.set(topics[0])  # default value

        topic_options = OptionMenu(
            self._frame, topic_var, *topics, command=self._topic_choice)
        topic_options.grid(padx=5, pady=5, sticky=constants.EW)

# aiheen valinta

        level_choice_label = ttk.Label(
            master=self._frame, text="Valitse vaikeustaso", font=('Helvetica', 12, 'bold'))
        level_choice_label.grid(padx=5, pady=5, sticky=constants.EW)

        difficulty_label = ttk.Label(
            master=self._frame, text=f"Valittu vaikeustaso: {taskservices.return_active_difficulty_str()}")
        difficulty_label.grid(padx=5, pady=5, sticky=constants.EW)

        difficulty = taskservices.return_difficulty_range()
        difficulty_var = StringVar()

        difficulty_var.set(difficulty[0])  # default value

        difficulty_options = OptionMenu(
            self._frame, difficulty_var, *difficulty, command=self._difficulty_choice)
        difficulty_options.grid(padx=5, pady=5, sticky=constants.EW)

        if topicservices.active_topic is not None and taskservices.active_difficulty is not None:
            start_task_button = ttk.Button(
                master=self._frame,
                text="Tee tehtäviä",
                command=self._handle_task
            )
            start_task_button.grid(padx=5, pady=5, sticky=constants.EW)

        result_button = ttk.Button(
            master=self._frame,
            text="Näytä tulokset",
            command=self._handle_result
        )
        result_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.pack()
