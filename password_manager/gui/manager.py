import tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, master):

        lbl_name = tk.Label(text='Password manager', font=('Helvetica', 24, 'bold'))
        lbl_name.grid(row = 0, column = 1, columnspan = 2, ipadx = 16, pady = (12, 6))

        lbl_name = tk.Label(text='Naam')
        lbl_name.grid(row = 1, column = 1, padx = 16, sticky='w')

        entry_name = tk.Entry()
        entry_name.grid(row = 1, column = 2, ipadx = 16)

        lbl_url = tk.Label(text='URL')
        lbl_url.grid(row = 2, column = 1, ipadx = 16, sticky='w')

        entry_url = tk.Entry()
        entry_url.grid(row = 2, column = 2, ipadx = 16)

        lbl_username = tk.Label(text='Username')
        lbl_username.grid(row = 3, column = 1, ipadx = 16, sticky='w')

        entry_username = tk.Entry()
        entry_username.grid(row = 3, column = 2, ipadx = 16)

        lbl_password = tk.Label(text='Password')
        lbl_password.grid(row = 4, column = 1, ipadx = 16, sticky='w')

        entry_password = tk.Entry()
        entry_password.grid(row = 4, column = 2, ipadx = 16)

        lbl_name = tk.Label(text='Password generator', font=('Helvetica', 24, 'bold'))
        lbl_name.grid(row = 5, column = 1, columnspan = 2, ipadx = 16, pady = (32, 6))

        lbl_length = tk.Label(text='Number of characters')
        lbl_length.grid(row = 6, column = 1, ipadx = 16, sticky='w')

        entry_length = tk.Entry(width = 6)
        entry_length.grid(row = 6, column = 2, ipadx = 16)

        lbl_uppercase = tk.Label(text='Number of uppercase')
        lbl_uppercase.grid(row = 7, column = 1, ipadx = 16, sticky='w')

        entry_uppercase = tk.Entry(width = 6)
        entry_uppercase.grid(row = 7, column = 2, ipadx = 16)

        lbl_lowercase = tk.Label(text='Number of lowercase')
        lbl_lowercase.grid(row = 8, column = 1, ipadx = 16, sticky='w')

        entry_lowercase = tk.Entry(width = 6)
        entry_lowercase.grid(row = 8, column = 2, ipadx = 16)

        lbl_digits = tk.Label(text='Number of digits')
        lbl_digits.grid(row = 9, column = 1, ipadx = 16, sticky='w')

        entry_digits = tk.Entry(width = 6)
        entry_digits.grid(row = 9, column = 2, ipadx = 16)

        lbl_special = tk.Label(text='Number of specials')
        lbl_special.grid(row = 10, column = 1, ipadx = 16, sticky='w')

        entry_special = tk.Entry(width = 6)
        entry_special.grid(row = 10, column = 2, ipadx = 16)

        btn_generate = tk.Button(text='Generate', font=('Helvetica', 16, 'bold'))
        btn_generate.grid(row = 11, column = 1, columnspan=2, pady = 16, ipadx = 8, ipady = 8)


if __name__ == '__main__':

    root = tk.Tk()

    root.geometry('410x480+100+100')  # width x height + x_offset + y_offset
    root.title('Password Manager')

    App(root)

    root.mainloop()
