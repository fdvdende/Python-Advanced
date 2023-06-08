from project_c.models.user import User
from project_c.models import exceptions
from project_c.models.persistence import Persistence

import tkinter as tk


class Frame1(tk.Frame):

    def __init__(self, master):
        super().__init__()

        self.master = master

        w = tk.Label(self, text='Gebruikers')
        w.grid(row=0, column=0, columnspan=2)

        user_names = []
        self.user_names = tk.Variable(value=user_names)
        self.users_list = tk.Listbox(self, listvariable = self.user_names)
        self.update_list()
        self.users_list.grid(row=1, column=0, columnspan=2)

        w = tk.Button(self, text='Toevoegen', command=self.handle_add)
        w.grid(row=2, column=0)

        w = tk.Button(self, text='Verwijderen', command=self.handle_remove)
        w.grid(row=2, column=1)

    def handle_add(self):
        self.master.show_frame2()

    def handle_remove(self):
        index = self.users_list.curselection()[0]
        user_name = self.user_names.get()[index]
        persistence = Persistence()
        persistence.remove_user(user_name)
        self.users_list.delete(index)

    def update_list(self):
        persistence = Persistence()
        user_names = persistence.get_user_names()
        self.users_list.delete(0, tk.END)
        self.users_list.insert(0, *user_names)


class Frame2(tk.Frame):

    def __init__(self, master):
        super().__init__()

        self.master = master

        w = tk.Label(self, text='Voer nieuwe gebruiker in')
        w.grid(row=0, column=0, columnspan=2)

        w = tk.Label(self, text='Naam')
        w.grid(row=1, column=0)

        self.name = tk.StringVar()
        w = tk.Entry(self, textvariable=self.name)
        w.grid(row=1, column=1)

        w = tk.Label(self, text='Wachtwoord')
        w.grid(row=2, column=0)

        self.password = tk.StringVar()
        w = tk.Entry(self, textvariable=self.password)
        w.grid(row=2, column=1)

        w = tk.Button(self, text='OK', command=self.handle_ok)
        w.grid(row=3, column=0)

        w = tk.Button(self, text='Cancel', command=self.handle_ok)
        w.grid(row=3, column=1)

    def handle_ok(self):
        user_name = self.name.get()
        user_password = self.password.get()

        persistence = Persistence()

        user = User(user_name)
        try:
            user.set_password(user_password)
        except exceptions.InvalidPasswordException:
            print('Dat wachtwoord voldoet niet aan de eisen.')

        persistence.save_user(user)

        self.name.set('')
        self.password.set('')

        self.master.frame1.update_list()

        self.master.show_frame1()

    def handle_cancel(self):
        self.name.set('')
        self.password.set('')
        self.master.show_frame1()


class App(tk.Frame):

    def __init__(self, master):
        super().__init__()

        self.frame2 = Frame2(self)
        self.frame2.grid(column=0, row=0, sticky='news')

        self.frame1 = Frame1(self)
        self.frame1.grid(column=0, row=0, sticky='news')

        self.show_frame1()

    def show_frame1(self):
        self.frame1.tkraise()

    def show_frame2(self):
        self.frame2.tkraise()


