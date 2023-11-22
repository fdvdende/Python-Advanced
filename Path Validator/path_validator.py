import tkinter as tk
from tkinter import filedialog
import os


class App(tk.Frame):
    MAX_FILENAME_LENGTH = 255

    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, master):

        # Title
        lbl_name = tk.Label(text='Path Validator', font=('Helvetica', 24, 'bold'))
        lbl_name.grid(row=1,
                      column=1,
                      columnspan=2,
                      pady=(12, 6))

        # Destination 10-19
        lbl_destination = tk.Label(text='Destination')
        lbl_destination.grid(row=10,
                             column=1,
                             columnspan=2,
                             padx=12,
                             pady=(12, 0),
                             sticky='w')

        self.destination = tk.StringVar()
        self.entry_destination = tk.Entry(textvariable=self.destination,
                                          width=40)
        self.entry_destination.grid(row=11,
                                    column=1,
                                    padx=12)

        btn_destination = tk.Button(text='📁',
                                    font=('Helvetica', 12, 'bold'),
                                    fg='#aa0000',
                                    command=self.handle_destination)
        btn_destination.grid(row=11,
                             column=2,
                             padx=(0, 12))

        # Remaining characters 20-29
        lbl_remaining = tk.Label(text='Remaining characters')
        lbl_remaining.grid(row=20,
                           column=1,
                           columnspan=2,
                           padx=12,
                           pady=(12, 0),
                           sticky='w')

        self.remaining = tk.StringVar()
        self.entry_remaining = tk.Entry(textvariable=self.remaining, width=4)
        self.entry_remaining.grid(row=21,
                                  column=1,
                                  padx=12,
                                  sticky='w')
        self.remaining.set(App.MAX_FILENAME_LENGTH)

        # Source 30-39
        lbl_source = tk.Label(text='Source')
        lbl_source.grid(row=30,
                        column=1,
                        columnspan=2,
                        padx=12,
                        pady=(12, 0),
                        sticky='w')

        self.source = tk.StringVar()
        self.entry_source = tk.Entry(textvariable=self.source,
                                     width=40)
        self.entry_source.grid(row=31,
                               column=1,
                               padx=12)

        btn_source = tk.Button(text='📁',
                               font=('Helvetica', 12, 'bold'),
                               fg='#aa0000',
                               command=self.handle_source)
        btn_source.grid(row=31,
                        column=2,
                        padx=(0, 12))

        # OK 40-49
        self.lbl_ok = tk.Label(text='OK or Not OK')
        self.lbl_ok.grid(row=40,
                         column=1,
                         padx=12,
                         pady=(12, 0),
                         sticky='w')

        # Store in file 50-59
        lbl_output = tk.Label(text='Store in file')
        lbl_output.grid(row=50,
                        column=1,
                        padx=12,
                        pady=(12, 0),
                        sticky='w')

        self.output = tk.StringVar()
        self.entry_output = tk.Entry(textvariable=self.output,
                                     width=40)
        self.entry_output.grid(row=51,
                               column=1,
                               padx=12)

        btn_output = tk.Button(text='📁',
                               font=('Helvetica', 12, 'bold'),
                               fg='#aa0000',
                               command=self.handle_output)
        btn_output.grid(row=51,
                        column=2,
                        padx=(0, 12))

        btn_export = tk.Button(text='Store',
                               font=('Helvetica', 18, 'bold'),
                               fg='#aa0000',
                               command=self.handle_store)
        btn_export.grid(row=52,
                        column=1,
                        padx=12,
                        pady=12,
                        columnspan=2)

    def handle_destination(self):
        file_path = filedialog.askdirectory()
        self.destination.set(file_path)
        self.remaining.set(App.MAX_FILENAME_LENGTH - len(file_path))

    def handle_source(self):
        path = filedialog.askdirectory()
        self.source.set(path)
        destination = self.destination.get()
        self.remaining.set(App.MAX_FILENAME_LENGTH - len(destination))
        remaining = int(self.remaining.get())
        self.to_long = []
        for absolute_path in self.get_recursive_list_of_files(path):
            if len(absolute_path) > remaining:
                self.to_long.append(absolute_path)
        if self.to_long:
            self.lbl_ok['text'] = f'NOT OK - {len(self.to_long)} are to long'
        else:
            self.lbl_ok['text'] = 'OK - All files can be copied'

    def handle_output(self):
        file_path = filedialog.asksaveasfilename()
        self.output.set(file_path)

    def handle_store(self):
        file_path = self.output.get()
        with open(file_path, 'w') as f:
            for filename in self.to_long:
                print(filename, file=f)

    @staticmethod
    def get_recursive_list_of_files(directory, max_length = None):
        for root, dir, files in os.walk(directory):
            for filename in files:
                absolute_path = os.path.join(root, filename)
                if max_length is None:
                    yield absolute_path
                elif len(absolute_path) > max_length:
                    yield absolute_path



if __name__ == '__main__':
    root = tk.Tk()

    # root.geometry('500x550+100+100')  # width x height + x_offset + y_offset
    root.title('Path Validator')
    root.resizable(width=False, height=False)

    App(root)

    root.mainloop()
