import tkinter as tk

from modelsX.equipment import Equipment

class App(tk.Frame):

    def __init__(self, master=None):

        equipment = Equipment.from_pickle()
        self.list = equipment.equipment

        w = tk.Label(master, text="Equipment", font=("Arial", 25))
        w.pack()

        list_var = tk.StringVar(value = self.list)
        w = tk.Listbox(master, listvariable = list_var, width = 60)
        w.pack()



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x500+100+100')  # width x height + x_offset + y_offset
    root.title('Equipment')
    app = App(root)
    root.mainloop()