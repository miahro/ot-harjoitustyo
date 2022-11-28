from tkinter import ttk, constants


class ChoiceView:
    def __init__(self, root, handle_start, handle_task, handle_result):
        self._root = root
        self._handle_start = handle_start
        self._handle_task = handle_task
        self._handle_result = handle_result
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Valintanäkymä")

        button = ttk.Button(
            master=self._frame,
            text="Palaa alkuun",
            command=self._handle_start
        )

        label.grid(row=5, column=0)
        button.grid(row=6, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Tee tehtäviä",
            command=self._handle_task
        )
        button.grid(row=10, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Näytä tulokset",
            command=self._handle_result
        )
        button.grid(row=15, column=0)

        self.pack()
