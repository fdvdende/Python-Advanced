from project_c.gui.app import App

import tkinter as tk


root = tk.Tk()
root.geometry('500x400+100+100')  # width x height + x_offset + y_offset
root.title('Secrets')
app = App(root)
root.mainloop()
