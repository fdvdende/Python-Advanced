import tkinter as tk

top = tk.Tk()

def hello():
     tk.MessageBox.showinfo("Say Hello", "Hello World")

btn1 = tk.Button(top, text = "Say Hello", command = hello)
btn1.pack()
top.mainloop()
