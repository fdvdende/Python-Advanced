import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):
        w = tk.Label(master, text="Hello, world!")
        w.pack()

        w = tk.Button(master, text="Klik hier")
        w.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()