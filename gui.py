from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window
        #
        self.name_frame = Frame(self.window)
        self.name_label = Label(self.name_frame, text='Student name:')
        self.name_entry = Entry(self.name_frame)
        self.name_label.pack(side='left', pady=5)
        self.name_entry.pack(side='left', pady=5)
        self.name_frame.pack(side='top')
        #
        self.attempts_frame = Frame(self.window)
        self.attempts_label = Label(self.attempts_frame, text='No of attempts:')
        self.attempts_entry = Entry(self.attempts_frame)
        self.attempts_label.pack(side='left',pady=5)
        self.attempts_entry.pack(side='left',pady=5)
        self.attempts_frame.pack(side='top', padx=5)
        #
        self.scores_frame = Frame(self.window)
        self.scores_frame.pack(side='top')
        #
        self.submit_button = Button(self.window, text='SUBMIT')
        self.submit_button.pack()
        #
        self.error_label = Label(self.window, text='', fg='red')
        self.error_label.pack()
        #
        self.score_boxes = []
        self.make_score_boxes()

    def error_message(self, error):
        self.error_label.config(text=error)

    def make_score_boxes(self):
        try:
            num = int(self.attempts_entry.get())
            if num not in [1,2,3,4]:
                raise ValueError
            self.error_message('')
        except ValueError:
            self.error_message('Invalid Entry')
            #return
        num = 4
        #
        for s in range(1, num+1):
            new_frame = Frame(self.scores_frame)
            new_label = Label(new_frame, text=f'Score {s}:')
            new_entry = Entry(new_frame, width=5)
            new_label.pack(side='left')
            new_entry.pack(side='left')
            new_frame.pack(side='top',anchor='e')
