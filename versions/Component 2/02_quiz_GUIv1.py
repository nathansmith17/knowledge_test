from tkinter import *
from functools import partial  # To prevent unwanted windows
# import random


class Menu:
    def __init__(self):
        # Formatting variables...
        background_color = "light yellow"

        # Converter main screen GUI...
        self.menu_frame = Frame(width=300, bg=background_color, pady=10)
        self.menu_frame.grid()

        # Temperature conversion Heading (row 0)
        self.knowledge_test_label = Label(self.menu_frame,
                                          text="Knowledge Test",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.knowledge_test_label.grid(row=0)

        self.button_frame = Frame(self.menu_frame)
        self.button_frame.grid(row=1, pady=10)

        # Start button (row 1 column 0)
        self.start_button = Button(self.button_frame, text="Start",
                                   font=("Arial", "14"),
                                   padx=10, pady=10,
                                   command=self.start)
        self.start_button.grid(row=0, column=0)

        # Help button (row 1)
        self.help_button = Button(self.button_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="Press the 'START' button to start"
                                          " the quiz. After it has finished, "
                                          "the quiz will save the results "
                                          "automatically. If you want to "
                                          "export the results to a .txt file,"
                                          " click 'EXPORT'.")

    def start(self):
        print("start")
        Quiz(self)


class Help:
    def __init__(self, partner):
        background = '#F8CECC'

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up gui Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg=background,
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Re-enables the help button
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Quiz:
    def __init__(self, partner):
        background = "#DAE8FC"

        # disable start button
        partner.start_button.config(state=DISABLED)

        # sets up child window
        self.start_box = Toplevel()

        self.start_box.protocol('WM_DELETE_WINDOW', partial(self.close_quiz,
                                                            partner))

        self.quiz_frame = Frame(self.start_box, width=400, height=375,
                                bg=background)
        self.quiz_frame.grid()

        # Heading (row 0)
        self.quiz_label = Label(self.quiz_frame,
                                text="Quiz", font="Arial 18 bold",
                                bg=background, padx=10, pady=10)
        self.quiz_label.grid(row=0)

        self.question_label = Label(self.quiz_frame,
                                    text="<ask question here>",
                                    font="Arial 12", wrap=250, pady=10,
                                    bg=background)
        self.question_label.grid(row=1)

    def close_quiz(self, partner):
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Menu()
    root.mainloop()
