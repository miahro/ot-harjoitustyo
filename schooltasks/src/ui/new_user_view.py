from tkinter import ttk, constants, StringVar
from services.user_services import userservices


class NewUserView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._message = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _new_user(self):
        first_name = self._first_name_entry.get()
        last_name = self._last_name_entry.get()
        user_id = self._user_id_entry.get()
        passwd1 = self._passwd_entry.get()
        passwd2 = self._passwd2_entry.get()

        result = userservices.create_new_user(
            first_name, last_name, user_id, passwd1, passwd2)
        self._show_message(result[1])
        self._clear_entry_fields()

    def _clear_entry_fields(self):
        self._first_name_entry.delete(0, 'end')
        self._last_name_entry.delete(0, 'end')
        self._user_id_entry.delete(0, 'end')
        self._passwd_entry.delete(0, 'end')
        self._passwd2_entry.delete(0, 'end')

    def _show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    # def _show_error(self, message):
    #     self._error.set(message)
    #     self._error_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()

    def _initialize_input_fields(self):

        first_name_label = ttk.Label(master=self._frame, text="Etunimi")
        self._first_name_entry = ttk.Entry(master=self._frame)
        first_name_label.grid(padx=5, pady=5, sticky=constants.W)
        self._first_name_entry.grid(padx=5, pady=5, sticky=constants.EW)

        last_name_label = ttk.Label(master=self._frame, text="Sukunimi")
        self._last_name_entry = ttk.Entry(master=self._frame)
        last_name_label.grid(padx=5, pady=5, sticky=constants.W)
        self._last_name_entry.grid(padx=5, pady=5, sticky=constants.EW)

        user_id_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._user_id_entry = ttk.Entry(master=self._frame)
        user_id_label.grid(padx=5, pady=5, sticky=constants.W)
        self._user_id_entry.grid(padx=5, pady=5, sticky=constants.EW)

        passwd_label = ttk.Label(master=self._frame, text="Salasana")
        self._passwd_entry = ttk.Entry(master=self._frame)
        passwd_label.grid(padx=5, pady=5, sticky=constants.W)
        self._passwd_entry.grid(padx=5, pady=5, sticky=constants.EW)

        passwd2_label = ttk.Label(
            master=self._frame, text="Salasana uudestaan")
        self._passwd2_entry = ttk.Entry(master=self._frame)
        passwd2_label.grid(padx=5, pady=5, sticky=constants.W)
        self._passwd2_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Uuden käyttäjän luonti")
        label.grid(row=0, column=0)

        self._message = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message,
            foreground='red'
        )
        self._message_label.grid(padx=5, pady=5)

        self._initialize_input_fields()

        new_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._new_user)
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        return_button = ttk.Button(
            master=self._frame,
            text="Palaa",
            command=self._handle_start
        )
        return_button.grid(padx=5, pady=5, sticky=constants.EW)

        # self._hide_message()
