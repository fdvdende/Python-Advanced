import tkinter as tk
# import pygame
import string

from models.game import Game

FONT = ("Helvetica", 26)


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self._game = Game()
        self._number_correct = 0

        # pygame.init()
        # self._sound = pygame.mixer.Sound('tada.mp3')
        # pygame.mixer.Sound.play(self._sound)

        master.configure(bg='darkred')

        w = tk.Label(master,
                     text=self._game.qa.question,
                     font=FONT,
                     fg='yellow',
                     bg='darkred',
                     pady=24)
        w.pack()

        self._points_labels = dict()
        self._keyword_labels = dict()
        for keyword in self._game.qa.keywords:

            row = tk.Frame()

            w = tk.Label(row,
                         text='$$',
                         font=FONT,
                         fg='#660000',
                         bg='darkred',
                         pady=12,
                         padx=30)
            w.visible = False
            w.pack(side = tk.LEFT)
            self._points_labels[keyword] = w

            w = tk.Label(row,
                         text=keyword.lower().translate(str.maketrans(string.ascii_lowercase, '▒'*len(string.ascii_lowercase), '')),
                         font=FONT,
                         fg='#660000',
                         bg='darkred',
                         pady=12)
            w.visible = False
            w.pack(side = tk.LEFT)
            self._keyword_labels[keyword] = w

            row.pack()

        def event_handler(event):
            PUNTEN_LADDER = [10, 20, 30, 40, 50]
            response = event.widget.get()
            event.widget.delete(0, len(response))
            keyword = self._game.qa.compare_to_keyword(response)
            print(response, keyword)
            if keyword:
                self._number_correct += 1
                self._keyword_labels[keyword].config(fg = 'yellow')
                self._keyword_labels[keyword].config(text = keyword)
                self._points_labels[keyword].config(fg='yellow')
                points = PUNTEN_LADDER[self._number_correct - 1]
                self._points_labels[keyword].config(text = str(points))


        self.input = tk.Entry(master, width=20, font=FONT)
        self.input.pack(side = tk.BOTTOM, pady = 20)
        self.input.bind('<Return>', event_handler)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
    root.title('Wat weet je van ... ?')
    app = App(root)
    root.mainloop()
