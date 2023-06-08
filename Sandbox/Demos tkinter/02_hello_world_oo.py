import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):
        w = tk.Label(master, text="Hello, world!", fg='red')
        w.grid(row = 0, sticky=tk.W)

        w = tk.Label(master, text="TWEEDE REGEL", fg='GREEN')
        w.grid(row = 1, sticky=tk.W)

        w = tk.Label(master, text="Derde", fg='GREEN')
        w.grid(row = 1, column = 1)


        w = tk.Button(master, text="Klik hier!")
        w.grid(row=2, column=1)

if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()