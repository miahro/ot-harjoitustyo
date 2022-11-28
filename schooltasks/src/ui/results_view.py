from tkinter import ttk, constants


class ResultView:
    def __init__(self, root, handle_start, handle_choice):
        self._root = root
        self._handle_start = handle_start
        self._handle_choice = handle_choice
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tulosnäkymä")
        button = ttk.Button(
            master=self._frame,
            text="Palaa alkuun",
            command=self._handle_start
        )

        label.grid(row=5, column=0)

        button.grid(row=6, column=0)

        button = ttk.Button(
            master=self._frame,
            text="Palaa takaisin",
            command=self._handle_choice
        )
        button.grid(row=10, column=0)

        self.pack()
