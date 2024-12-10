from tkinter import *
import csv

class Gui:
    def __init__(self, window) -> None:
        """
        initializes an instance of the score submission gui
        :param window: None
        """
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

        options_list: list = ['1','2','3','4']
        self.selected = StringVar(self.window)
        self.selected.set('')
        self.selected.trace('w',self.make_score_boxes)
        self.attempts_optionmenu = OptionMenu(self.attempts_frame, self.selected, *options_list)
        self.attempts_label.pack(side='left',pady=5)
        self.attempts_optionmenu.pack(side='left',pady=5)
        self.attempts_frame.pack(side='top', padx=5)
        #
        self.scores_frame = Frame(self.window)
        self.scores_frame.pack(side='top')
        #
        self.submit_button = Button(self.window, text='SUBMIT',command=self.submit)
        self.submit_button.pack()
        #
        self.error_label = Label(self.window, text='', fg='red')
        self.error_label.pack()
        #
        self.score_frames: list = []
        self.score_entries: list = []

    def error_message(self, text) -> None:
        """
        edits the text of the error label to be whatever the variable
        text is
        :param text: str
        :return: None
        """
        self.error_label.config(text=text)

    def make_score_boxes(self, *args):
        """
        Destorys all of the current score boxes and generates
        a number of new ones equal to that of the value from the
        dropdown menu
        :param args:
        :return: None
        """
        self.error_message('')
        try:
            num = int(self.selected.get())
        except ValueError:
            return
        for score_frame in self.score_frames:
            score_frame.destroy()
        self.score_frames = []
        self.score_entries = []
        #
        for s in range(1, num+1):
            new_frame = Frame(self.scores_frame)
            new_label = Label(new_frame, text=f'Score {s}:')
            new_entry = Entry(new_frame, width=5)
            new_label.pack(side='left')
            new_entry.pack(side='left')
            new_frame.pack(side='top',anchor='e')
            self.score_frames.append(new_frame)
            self.score_entries.append(new_entry)

    def submit(self):
        self.error_message('')
        new_row = []
        #
        name = self.name_entry.get().strip()
        if name == '':
            self.error_message('Invalid Name Entry')
            return
        else:
            new_row.append(name)
        if self.selected.get() == '':
            self.error_message('Please select number of scores')
            return
        #
        for i in range(4):
            try:
                score = int(self.score_entries[i].get().strip())
                if score < 0 or score > 100:
                    raise ValueError
            except IndexError:
                score = 0
            except ValueError:
                self.error_message('Invalid Score Value(s)')
                return
            new_row.append(score)
        high_score = max(new_row[1:])
        new_row.append(high_score)

        file = open('grades.csv', 'a', newline='')
        csv_writer = csv.writer(file)
        csv_writer.writerow(new_row)
        file.close()
        self.error_message('Scores Submitted')