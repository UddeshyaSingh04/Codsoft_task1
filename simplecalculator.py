import tkinter as tk


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_equal():
    try:
        global expression
        result = str(eval(expression)) 
        input_text.set(result) 
        expression = "" 
    except:
        input_text.set("Error")
        expression = ""

def button_clear():
    global expression
    expression = ""
    input_text.set("")


root = tk.Tk()
root.title("Simple Calculator")


root.configure(bg="light blue")
root.geometry("300x400")
root.resizable(False, False)


expression = ""


input_text = tk.StringVar()


entry = tk.Entry(root, textvariable=input_text, justify='right', font=('Arial', 24), bd=10, relief=tk.SOLID)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10, sticky="nsew")


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, column) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'),
                  command=button_equal, bg="green").grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'),
                  command=button_clear, bg="orange").grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'),
                  command=lambda text=text: button_click(text)).grid(row=row, column=column, padx=5, pady=5, sticky="nsew")


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1) 

root.mainloop()
