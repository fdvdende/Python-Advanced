import tkinter as tk

from src.gui.tkinter_gui import App

root = tk.Tk()
root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
root.title('Wat weet je van ... ?')
app = App(root)
root.mainloop()