from tkinter import *


if __name__ == "__main__":

    # everything is a widget
    # first widget is always root

    root = Tk()

    # simple window

    # create label widget
    label = Label(master=root, text="Hello world!")
    # simplest way to add label to window is .pack
    # creates a minimal window for the content that is added
    label.pack()

    # create an event loop
    root.mainloop()