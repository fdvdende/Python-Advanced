import tkinter as tk

from src.gui.app import App


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('500x400+300+300')  # width x height + x_offset + y_offset
    root.title('Secrets')
    app = App(root)
    root.mainloop()
