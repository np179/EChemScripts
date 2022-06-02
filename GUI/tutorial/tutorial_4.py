from tkinter import *

# build a simple calculator
# well it was simple in the beginning

def button_add(input: int):
    if "=" in e.get().split(" "):
        e.delete(0, END)
    e.insert(END, input)

def clear():
    e.delete(0, END)

def clean(ls: list, idx: int, result: float) -> list:
    """Convenience function to remove elements
    of evaluated subexpressions from the expression."""


    ls[idx] = result
    del ls[idx-1]
    # since we remove the i-1th element i+1 becomes i
    del ls[idx]
    return ls

def find_op(case: list, expression: list) -> list:
    """Find and evaluate all expressions for a given operator,
    removing evaluated expressions and leaving only the result."""

    while bool([op for op in case if(op in expression)]):
        # print(expression)
        # print(len(expression))
        for i, elem in enumerate(expression):
            # print("1", i, elem)
            if elem in case and elem == "x":
                result = float(expression[i-1]) * float(expression[i+1])
                expression = clean(expression, i, result)
                break
            elif elem in case and elem == "/":
                result = float(expression[i-1]) / float(expression[i+1])
                expression = clean(expression, i, result)
                break
            elif elem in case and elem == "+":
                # for j, elem in enumerate(expression):
                #     print("2", j, elem)
                result = float(expression[i-1]) + float(expression[i+1])
                expression = clean(expression, i, result)
                break
            elif elem in case and elem == "-":
                result = float(expression[i-1]) - float(expression[i+1])
                expression = clean(expression, i, result)
                break
        print("Solving all '{}' subexpressions.".format([op for op in case]))
        print(" ".join([str(elem) for elem in expression]))
    print("Solved all '{}' subexpressions.".format([op for op in case]))
    return expression

def eval():
    """Evaluate the whole expression."""

    # get the expression
    expression = e.get()
    split_ex = expression.split(" ")

    print("Initial expression:")
    print(" ".join([str(elem) for elem in split_ex]))

    # order in which we want to evaluate these operators
    # x and / before - and + but from left to right in the
    # respective cases
    operators = [["x", "/"], ["-", "+"]]
   
    for case in operators:
        print("Searching for {}".format(" ".join([op for op in case])))
        split_ex = find_op(case, split_ex)
        if len(split_ex) == 1:
            result = split_ex[0]
            # return integer if result is integer
            if result.is_integer():
                result = int(result)

    e.insert(END, " = " + str(result))


if __name__ == "__main__":

    root = Tk()

    # set the title
    root.title("Calculator")

    e = Entry(master=root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

    button1 = Button(master=root, text="1", padx=40, pady=20, command=lambda: button_add(1)).grid(row=3, column=0)
    button2 = Button(master=root, text="2", padx=40, pady=20, command=lambda: button_add(2)).grid(row=3, column=1)
    button3 = Button(master=root, text="3", padx=40, pady=20, command=lambda: button_add(3)).grid(row=3, column=2)
    button4 = Button(master=root, text="4", padx=40, pady=20, command=lambda: button_add(4)).grid(row=2, column=0)
    button5 = Button(master=root, text="5", padx=40, pady=20, command=lambda: button_add(5)).grid(row=2, column=1)
    button6 = Button(master=root, text="6", padx=40, pady=20, command=lambda: button_add(6)).grid(row=2, column=2)
    button7 = Button(master=root, text="7", padx=40, pady=20, command=lambda: button_add(7)).grid(row=1, column=0)
    button8 = Button(master=root, text="8", padx=40, pady=20, command=lambda: button_add(8)).grid(row=1, column=1)
    button9 = Button(master=root, text="9", padx=40, pady=20, command=lambda: button_add(9)).grid(row=1, column=2)
    button0 = Button(master=root, text="0", padx=40, pady=20, command=lambda: button_add(0)).grid(row=4, column=1)
    
    button_ad = Button(master=root, text="+", padx=36, pady=20, command=lambda: button_add(" + ")).grid(row=1, column=3)
    button_sub = Button(master=root, text="-", padx=37, pady=20, command=lambda: button_add(" - ")).grid(row=2, column=3)
    button_mul = Button(master=root, text="x", padx=37, pady=20, command=lambda: button_add(" x ")).grid(row=3, column=3)
    button_div = Button(master=root, text="/", padx=38, pady=20, command=lambda: button_add(" / ")).grid(row=4, column=3)
    
    button_equal = Button(master=root, text="=", padx=39, pady=20, command=lambda: eval()).grid(row=4, column=2)
    button_clear = Button(master=root, text="CE", padx=36, pady=20, command=clear).grid(row=4, column=0)

    root.mainloop()