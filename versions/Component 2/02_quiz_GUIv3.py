from tkinter import *
from tkinter import messagebox as mb
from functools import partial  # To prevent unwanted windows
import json
import random

# with open('quiz.json') as f:
#     obj = json.load(f)
# q = (obj['ques'])
# options = (obj['options'])
# a = (obj['ans'])
# z = zip(q, options, a)
# l = list(z)
ans = []
# random.shuffle(l)
# q, options, a = zip(*l)


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

        self.quiz_frame = Frame(self.start_box, width=800, height=500,
                                bg=background)
        self.quiz_frame.grid()

        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radio_btns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(self.quiz_frame, text="Quiz in Python Programming",
                  width=50, bg="#DAE8FC",
                  fg="white", font=("Arial", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(self.quiz_frame, text=q[qn], width=60,
                   font=("Arial", 16, "bold"),
                   anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radio_btns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(self.quiz_frame, text=" ",
                              variable=self.opt_selected,
                              value=val + 1, font=("Arial", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        n_button = Button(self.quiz_frame, text="Next", command=self.next_btn,
                          width=10,
                          bg="green", fg="white", font=("Arial", 16, "bold"))
        n_button.place(x=200, y=380)
        quit_button = Button(self.quiz_frame, text="Quit",
                             command=self.quiz_frame.destroy, width=10,
                             bg="red", fg="white", font=("Arial", 16, "bold"))
        quit_button.place(x=380, y=380)

    def check_ans(self, qn):
        ans.append(self.opt_selected.get())
        if self.opt_selected.get() == a[qn]:
            return True

    def next_btn(self):
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 200)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

    def close_quiz(self, partner):
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Menu()
    root.mainloop()
