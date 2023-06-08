import tkinter as tk

class App:

    def __init__(self, master):

        frame = tk.Frame(master, width=300, height=300, bg='white')
        frame.pack()

        self.button = tk.Button(frame,
                                text="QUIT",
                                fg="red",
                                command=frame.quit)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame,
                                  text="Hello",
                                  command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    app = App(root)
    root.mainloop()
