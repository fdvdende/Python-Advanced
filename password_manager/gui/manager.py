import tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, master):

        lbl_name = tk.Label(text='Naam', justify=tk.LEFT)
        lbl_name.grid(row = 1, column = 1, ipadx = 16)

        entry_name = tk.Entry()
        entry_name.grid(row = 1, column = 2, ipadx = 16)

        lbl_url = tk.Label(text='URL')
        lbl_url.grid(row = 2, column = 1, ipadx = 16)

        entry_url = tk.Entry()
        entry_url.grid(row = 2, column = 2, ipadx = 16)

        lbl_username = tk.Label(text='Username')
        lbl_username.grid(row = 3, column = 1, ipadx = 16)

        entry_username = tk.Entry()
        entry_username.grid(row = 3, column = 2, ipadx = 16)

        lbl_password = tk.Label(text='Password')
        lbl_password.grid(row = 4, column = 1, ipadx = 16)

        entry_password = tk.Entry()
        entry_password.grid(row = 4, column = 2, ipadx = 16)





if __name__ == '__main__':

    root = tk.Tk()

    root.geometry('300x400+100+100')  # width x height + x_offset + y_offset
    root.title('Password Manager')

    App(root)

    root.mainloop()
