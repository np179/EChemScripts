import tkinter as tk
from tkinter import filedialog

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

if __name__ == "__main__":

    root = tk.Tk()
    folder_path = tk.StringVar()
    lbl1 = tk.Label(master=root,textvariable=folder_path)
    lbl1.grid(row=0, column=1)
    button2 = tk.Button(text="Browse", command=browse_button)
    button2.grid(row=0, column=3)

    tk.mainloop()