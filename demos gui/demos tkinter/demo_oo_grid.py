import tkinter as tk
import tkinter.messagebox

class App(tk.Frame):

    def __init__(self, master=None):
        self.teller = 0

        w = tk.Label(master, text="Hello, world!")
        w.grid(row = 1, column = 1, columnspan = 2)

        w = tk.Button(master, text="Klik hier", command=self.click_handler)
        w.grid(row = 2, column = 1, columnspan = 2)

        w = tk.Label(master, text="Getal 1")
        w.grid(row = 3, column = 1)

        self.text1 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text1)
        w.grid(row = 3, column = 2)

        w = tk.Label(master, text="Getal 2")
        w.grid(row = 4, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 4, column = 2)

        w = tk.Button(master, text="Tel op", command=self.telop)
        w.grid(row = 5, column = 1, columnspan = 2)

        w = tk.Label(master, text="Totaal")
        w.grid(row = 6, column = 1)

        self.result = tk.StringVar()
        w = tk.Entry(master, textvariable=self.result)
        w.grid(row = 6, column = 2)

        self.error_message = tk.Label(master, text="", fg='#F00')
        self.error_message.grid(row = 7, column = 1, columnspan = 2)
        # self.error_message.pack()
        # self.error_message.pack_forget()

    def click_handler(self):
        self.teller += 1
        print(f'BUTTON CLICKED!!! => {self.teller}')

    def telop(self):

        s = self.text1.get()
        if not self.validate(s):
            print('Getal 1 is niet goed')
            # tk.messagebox.showerror('Fout', 'Getal 1 is niet goed')
            self.error_message.config(text='Getal 1 is niet goed')
            # self.error_message.pack()
            return
        getal1 = int(s)

        s = self.text2.get()
        if not self.validate(s):
            print('Getal 2 is niet goed')
            # tk.messagebox.showerror('Fout', 'Getal 2 is niet goed')
            self.error_message.config(text='Getal 2 is niet goed')
            # self.error_message.pack()
            return
        getal2 = int(s)

        self.result.set(str(getal1 + getal2))
        print(f'de som is => {getal1 + getal2}')

    def validate(self, ingevoerd_tekst):
        try:
            waarde = int(ingevoerd_tekst)
            return True
        except ValueError:
            return False

        # if s.isnumeric():
        #     return True
        # else:
        #     return False



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()