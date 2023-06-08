import tkinter as tk

from ..domain.todo import Status, ToDo
from ..database import database_sqlite as database

class App(tk.Frame):

    def __init__(self, master=None):

        padding = dict(padx=30, pady=6)

        w = tk.Label(master, text="ToDo", font=("Arial", 25))
        w.grid(row = 1, column = 1, columnspan = 2, **padding)

        # Note
        w = tk.Label(master, text="Note")
        w.grid(row = 2, column = 1, **padding)

        self.note = tk.StringVar()
        w = tk.Entry(master, textvariable=self.note)
        w.grid(row = 2, column = 2, **padding)

        # Deadline
        w = tk.Label(master, text="Deadline")
        w.grid(row = 3, column = 1, **padding)

        self.deadline = tk.StringVar()
        w = tk.Entry(master, textvariable=self.deadline)
        w.grid(row = 3, column = 2, **padding)

        # Prioriteit
        w = tk.Label(master, text="Prioriteit")
        w.grid(row = 4, column = 1, **padding)

        self.prioriteit = tk.StringVar()
        w = tk.Entry(master, textvariable=self.prioriteit)
        w.grid(row = 4, column = 2, **padding)

        # Status
        print(Status)
        print(list(Status))
        self.status_options = {item.name: item for item in list(Status)}

        w = tk.Label(master, text="Status")
        w.grid(row = 5, column = 1, **padding)

        self.status = tk.StringVar()
        self.status.set(list(self.status_options.keys())[0])
        w = tk.OptionMenu(master, self.status, *self.status_options.keys())
        w.config(width=16)
        w.grid(row = 5, column = 2, **padding)

        # Active
        w = tk.Label(master, text="Active")
        w.grid(row = 6, column = 1, **padding)

        self.active = tk.StringVar()
        self.active.set(1)
        w = tk.Checkbutton(master, text='Active', variable=self.active, onvalue=1, offvalue=0)
        w.grid(row = 6, column = 2, **padding)

        w = tk.Button(master, text="Sla op", command=self.click_handler)
        w.grid(row = 7, column = 1, columnspan = 2, **padding)

    def reset(self):
        self.note.set(''),
        self.deadline.set(''),
        self.prioriteit.set(''),
        self.status.set(list(self.status_options.keys())[0]),
        self.active.set(1)

    def click_handler(self):
        todo = ToDo(self.note.get(),
                    self.deadline.get(),
                    self.prioriteit.get(),
                    self.status_options.get(self.status.get()),
                    self.active.get()
                    )
        database.add(todo)
        self.reset()

        print(list(database.get_all()))


def main():
    root = tk.Tk()
    # root.geometry('500x400+100+100')  # width x height + x_offset + y_offset
    root.title('ToDo application')
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
