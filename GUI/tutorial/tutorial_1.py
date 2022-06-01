from tkinter import *


if __name__ == "__main__":

    # everything is a widget
    # first widget is always root

    root = Tk()

    # create multiple labels
    label1 = Label(master=root, text="This is a label.")
    label2 = Label(master=root, text="This is another label.")
    # use the .grid method
    # grid is relative, i.e. if there is no column 2,3 or 4 putting column 5 goes to 2
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)

    # combine
    # label1 = Label(master=root, text="This is a label.").grid(row=0, column=0)
    # label2 = Label(master=root, text="This is another label.").grid(row=1, column=0)

    # create an event loop
    root.mainloop()