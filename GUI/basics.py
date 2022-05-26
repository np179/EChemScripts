import tkinter as tk

if __name__ == "__main__":

    window = tk.Tk()
    greeting = tk.Label(text="Hello World")
    greeting.pack()

    label = tk.Label(
        text = "Hello, Tinker",
        fg = "white",
        bg = "black"
    )
    label.pack()

    button = tk.Button(
        text = "Click me!",
        width = 25,
        height = 5,
        bg = "blue",
        fg = "yellow"
    )
    button.pack()

    label = tk.Label(text="Provide some text:")
    label.pack()

    entry = tk.Entry(
        fg = "yellow",
        bg = "blue",
        width = 50
    )
    entry.pack()


    window.mainloop()