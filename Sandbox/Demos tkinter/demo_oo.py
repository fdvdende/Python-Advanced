import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):
        self.teller = 0

        w = tk.Label(master, text="Hello, world!")
        w.pack()

        w = tk.Button(master, text="Klik hier", command=self.click_handler)
        w.pack()

        self.text1 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text1)
        w.pack()

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.pack()

        w = tk.Button(master, text="Tel op", command=self.telop)
        w.pack()

        self.result = tk.StringVar()
        w = tk.Entry(master, textvariable=self.result)
        w.pack()

    def click_handler(self):
        self.teller += 1
        print(f'BUTTON CLICKED!!! => {self.teller}')

    def telop(self):
        getal1 = int(self.text1.get())
        getal2 = int(self.text2.get())
        self.result.set(str(getal1 + getal2))
        print(f'de som is => {getal1 + getal2}')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()