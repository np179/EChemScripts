from tkinter import *

# build a simple calculator

def button_add():
    return

if __name__ == "__main__":
    root = Tk()

    # set the title
    root.title("Calculator")

    e = Entry(master=root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

    button1 = Button(master=root, text="1", padx=40, pady=20, command=button_add).grid(row=3, column=0)
    button2 = Button(master=root, text="2", padx=40, pady=20, command=button_add).grid(row=3, column=1)
    button3 = Button(master=root, text="3", padx=40, pady=20, command=button_add).grid(row=3, column=2)
    button4 = Button(master=root, text="4", padx=40, pady=20, command=button_add).grid(row=2, column=0)
    button5 = Button(master=root, text="5", padx=40, pady=20, command=button_add).grid(row=2, column=1)
    button6 = Button(master=root, text="6", padx=40, pady=20, command=button_add).grid(row=2, column=2)
    button7 = Button(master=root, text="7", padx=40, pady=20, command=button_add).grid(row=1, column=0)
    button8 = Button(master=root, text="8", padx=40, pady=20, command=button_add).grid(row=1, column=1)
    button9 = Button(master=root, text="9", padx=40, pady=20, command=button_add).grid(row=1, column=2)
    button0 = Button(master=root, text="0", padx=40, pady=20, command=button_add).grid(row=4, column=1)
    
    button_ad = Button(master=root, text="+", padx=37, pady=20, command=button_add).grid(row=1, column=4)
    button_sub = Button(master=root, text="-", padx=38, pady=20, command=button_add).grid(row=2, column=4)
    button_mul = Button(master=root, text="x", padx=39, pady=20, command=button_add).grid(row=3, column=4)
    button_div = Button(master=root, text="/", padx=39, pady=20, command=button_add).grid(row=4, column=4)
    
    button_equal = Button(master=root, text="=", padx=39, pady=20, command=button_add).grid(row=4, column=2)
    button_clear = Button(master=root, text="CE", padx=36, pady=20, command=button_add).grid(row=4, column=0)

    root.mainloop()