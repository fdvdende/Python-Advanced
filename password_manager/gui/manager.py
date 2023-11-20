from password_manager.password_manager.passwords.password_generator import generate_password
from password_manager.persistence.store_as_pickle import store


import tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, master):

        lbl_name = tk.Label(text='Password manager', font=('Helvetica', 24, 'bold'))
        lbl_name.grid(row = 0, column = 1, columnspan = 2, ipadx = 16, pady = (12, 6))

        lbl_name = tk.Label(text='Naam')
        lbl_name.grid(row = 1, column = 1, padx = 16, sticky='w')

        self.name = tk.StringVar()
        self.entry_name = tk.Entry(textvariable = self.name)
        self.entry_name.grid(row = 1, column = 2, ipadx = 16)

        lbl_url = tk.Label(text='URL')
        lbl_url.grid(row = 2, column = 1, ipadx = 16, sticky='w')

        self.url = tk.StringVar()
        self.entry_url = tk.Entry(textvariable = self.url)
        self.entry_url.grid(row = 2, column = 2, ipadx = 16)

        lbl_username = tk.Label(text='Username')
        lbl_username.grid(row = 3, column = 1, ipadx = 16, sticky='w')

        self.username = tk.StringVar()
        self.entry_username = tk.Entry(textvariable = self.username)
        self.entry_username.grid(row = 3, column = 2, ipadx = 16)

        lbl_password = tk.Label(text='Password')
        lbl_password.grid(row = 4, column = 1, ipadx = 16, sticky='w')

        self.password = tk.StringVar()
        self.entry_password = tk.Entry(textvariable = self.password)
        self.entry_password.grid(row = 4, column = 2, ipadx = 16)

        btn_generate = tk.Button(text='Store',
                                 font=('Helvetica', 18, 'bold'),
                                 fg='#aa0000',
                                 command=self.store_handler)
        btn_generate.grid(row = 5, column = 1, columnspan=2, pady = 16, ipadx = 8, ipady = 8)

        lbl_name = tk.Label(text='Password generator', font=('Helvetica', 24, 'bold'))
        lbl_name.grid(row = 6, column = 1, columnspan = 2, ipadx = 16, pady = (12, 6))

        lbl_length = tk.Label(text='Number of characters')
        lbl_length.grid(row = 7, column = 1, ipadx = 16, sticky='w')

        # entry_length = tk.Entry(width = 6)
        self.entry_length = tk.Scale(master, from_=4, to=20, orient=tk.HORIZONTAL)
        self.entry_length.set(8)
        self.entry_length.grid(row = 7, column = 2, ipadx = 16, sticky='w')

        lbl_uppercase = tk.Label(text='Number of uppercase')
        lbl_uppercase.grid(row = 8, column = 1, ipadx = 16, sticky='w')

        self.uppercase = tk.StringVar()
        self.entry_uppercase = tk.Entry(width = 6, textvariable = self.uppercase)
        self.uppercase.set(2)
        self.entry_uppercase.grid(row = 8, column = 2, ipadx = 16, sticky='w')

        lbl_lowercase = tk.Label(text='Number of lowercase')
        lbl_lowercase.grid(row = 9, column = 1, ipadx = 16, sticky='w')

        self.lowercase = tk.StringVar()
        self.entry_lowercase = tk.Entry(width = 6, textvariable = self.lowercase)
        self.lowercase.set(2)
        self.entry_lowercase.grid(row = 9, column = 2, ipadx = 16, sticky='w')

        lbl_digits = tk.Label(text='Number of digits')
        lbl_digits.grid(row = 10, column = 1, ipadx = 16, sticky='w')

        self.digits = tk.StringVar()
        self.entry_digits = tk.Entry(width = 6, textvariable = self.digits)
        self.digits.set(1)
        self.entry_digits.grid(row = 10, column = 2, ipadx = 16, sticky='w')

        lbl_special = tk.Label(text='Number of specials')
        lbl_special.grid(row = 11, column = 1, ipadx = 16, sticky='w')

        self.special = tk.StringVar()
        self.entry_special = tk.Entry(width = 6, textvariable = self.special)
        self.special.set(1)
        self.entry_special.grid(row = 11, column = 2, ipadx = 16, sticky='w')

        btn_generate = tk.Button(text='Generate',
                                 font=('Helvetica', 18, 'bold'),
                                 fg='#aa0000',
                                 command = self.generate_handler)
        btn_generate.grid(row = 12, column = 1, columnspan=2, pady = 16, ipadx = 8, ipady = 8)


    def generate_handler(self):
        print('Generate button pressed')
        settings = {
            'required_length': int(self.entry_length.get()),
            'n_lowercase': int(self.lowercase.get()),
            'n_uppercase': int(self.uppercase.get()),
            'n_numbers': int(self.digits.get()),
            'n_special': int(self.special.get())
        }
        password = generate_password(**settings)
        print(password)
        self.password.set(password)

    def store_handler(self):
        d = {
            'name': self.name.get(),
            'url': self.url.get(),
            'username': self.username.get(),
            'password': self.password.get()
        }
        store(d)


if __name__ == '__main__':

    root = tk.Tk()

    root.geometry('410x550+100+100')  # width x height + x_offset + y_offset
    root.title('Password Manager')
    root.resizable(width = False, height = False)

    App(root)

    root.mainloop()
