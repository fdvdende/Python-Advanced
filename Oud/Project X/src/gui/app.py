import tkinter as tk

from ..models.secret import Secret
from ..models.persistence import PersistenceWithSQLite

class App(tk.Frame):

    def __init__(self, master):
        super().__init__()

        w = tk.Label(master, text='Voer een geheim in.')
        w.grid(row=0, column=0, columnspan=2)

        w = tk.Label(master, text='Naam')
        w.grid(row=1, column=0, sticky=tk.W)

        self.name = tk.StringVar()
        w = tk.Entry(master, textvariable=self.name)
        w.grid(row=1, column=1, sticky=tk.W)

        w = tk.Label(master, text='Content')
        w.grid(row=2, column=0, sticky=tk.W)

        self.content = tk.StringVar()
        w = tk.Entry(master, textvariable=self.content)
        w.grid(row=2, column=1, sticky=tk.W)

        w = tk.Label(master, text='Owner')
        w.grid(row=3, column=0, sticky=tk.W)

        self.owner = tk.StringVar()
        w = tk.Entry(master, textvariable=self.owner)
        w.grid(row=3, column=1, sticky=tk.W)

        w = tk.Button(master, text='Opslaan', command=self.handle_click)
        w.grid(row=4, column=0, columnspan=2)

    def handle_click(self):
        name = self.name.get()
        content = self.content.get()
        owner = self.owner.get()

        self.name.set('')
        self.content.set('')
        self.owner.set('')

        secret = Secret(name, content, owner)

        PersistenceWithSQLite.store_secret(secret)