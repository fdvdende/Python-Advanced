#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.geometry('800x600+100+100')  # width x height + x_offset + y_offset
app.master.title('Sample application')
app.mainloop()