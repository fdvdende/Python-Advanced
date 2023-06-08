import sys

import tkinter
import tkinter.messagebox as mbox
import tkinter.simpledialog as sd

# to hide main window
window = tkinter.Tk()
window.wm_withdraw() 

tekst = sd.askstring( title="Input", prompt="Email Address?")

mbox.showinfo(title = "Greetings", message = tekst)
