from tkinter import *
from tkinter import ttk

expressions = ""
result = ""

def get_entry():
    global expressions
    global result
    expressions = entry.get()
    result = calculator(expressions)
    label2 = Label(text=result)
    label2.pack(anchor=NW,padx=6,pady=6)
    return expressions





def calculator(expression):
    allowed = "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(f"Выражение должно хотя - бы содержать 1 знак {allowed}")
    
    for sign in allowed:
        if sign in expression:
            try:
                left,rigth = expression.split(sign)
                left,rigth = int(left), int(rigth)
                return{
                    "*": lambda a,b: a * b,
                    "+": lambda a,b : a +b,
                    "-" : lambda a,b: a - b,
                    "/": lambda a,b: a / b
                    
                }[sign](left,rigth)
            except (ValueError,TypeError):
                raise ValueError(f"Выражение должно иметь максимум 1 символ {allowed}, и две целых чисел")



root = Tk()
root.geometry(("300x300"))
root.title("Calculator")
label = ttk.Label(text="Введите число: ")
label.pack(anchor=NW,padx=6,pady=6)

entry = ttk.Entry(font=("Arial",14))
entry.pack(anchor=NW,padx=6,pady=6)


button = ttk.Button(text="Result",command=get_entry)
button.pack(anchor=NW,padx=6,pady=6)


root.mainloop()
