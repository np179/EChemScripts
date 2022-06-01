from tkinter import *

def myClick():
    label = Label(master=root, text="Look! I clicked a Button!").pack()

if __name__ == "__main__":

    # everything is a widget
    # first widget is always root

    root = Tk()

    # create a button
    
    # disable
    # button = Button(master=root, text="Click Me!", state=DISABLED).pack()

    # resize
    # button = Button(master=root, text="Click me!", padx=50, pady=50).pack()

    # attach function to make button do something
    # dont call function in the command, so no myClick()
    # button = Button(master=root, text="Click me!", command=myClick).pack()

    # change colour
    # can use hexcolours
    button = Button(master=root, text="Click me!", command=myClick, fg="blue", bg="yellow").pack()


    # create an event loop
    root.mainloop()