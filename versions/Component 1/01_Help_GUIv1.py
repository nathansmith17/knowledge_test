from tkinter import *



class Converter:
    def __init__(self):
        print("welcome")

        # Formatting variables...
        background_color = "light yellow"

        # Converter main screen GUI...
        self.menu_frame = Frame(width=300,
                                height=300,
                                bg=background_color)
        self.menu_frame.grid()

        # Temperature conversion Heading (row 0)
        self.knowledge_test_label = Label(text="Knowledge Test",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.knowledge_test_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.menu_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Knowledge Test")
    something = Converter()
    root.mainloop()
