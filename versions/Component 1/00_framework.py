from tkinter import *
# import random


class Converter:
    def __init__(self):
        print("hello world")

        # Formatting variables...
        background_color = "light blue"

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Knowledge Test")
    something = Converter()
    root.mainloop()
