from tkinter import *


def myClick():
    message = "Hello " + e.get() + "!"
    label = Label(master=root, text=message).pack()


if __name__ == "__main__":

    # everything is a widget
    # first widget is always root

    root = Tk()

    query = Label(master=root, text="Provide a name:").pack()

    # create an entry widget
    # cant just pack the Entry in one line for some reason
    e = Entry(master=root)
    e.pack()

    # add insert, kinda weird example here though
    # e.insert(0, "Enter here")
    
    # some paramters
    # entry = Entry(master=root, width=50, bg="white", fg="black", border=5).pack()

    # create a button

    button = Button(master=root, text="Submit", command=myClick).pack()


    # create an event loop
    root.mainloop()