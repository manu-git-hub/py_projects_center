from tkinter import *
import parser

root = Tk()
root.title('Calculator')
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

i = 0


def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)


def undo1():
    entire_string = display.get()
    if entire_string:
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, 'Error')


def get_operator(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length


def calculate1():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')


Button(text=' 7 ', command=lambda: get_variable(7)).grid(row=2, column=0)
Button(text=' 8 ', command=lambda: get_variable(8)).grid(row=2, column=1)
Button(text=' 9 ', command=lambda: get_variable(9)).grid(row=2, column=2)
Button(text=' 4 ', command=lambda: get_variable(4)).grid(row=3, column=0)
Button(text=' 5 ', command=lambda: get_variable(5)).grid(row=3, column=1)
Button(text=' 6 ', command=lambda: get_variable(6)).grid(row=3, column=2)
Button(text=' 1 ', command=lambda: get_variable(1)).grid(row=4, column=0)
Button(text=' 2 ', command=lambda: get_variable(2)).grid(row=4, column=1)
Button(text=' 3 ', command=lambda: get_variable(3)).grid(row=4, column=2)
Button(text=' 0 ', command=lambda: get_variable(0)).grid(row=5, column=0)
Button(text='A C', command=lambda: clear_all()).grid(row=5, column=1)
Button(text=' = ', command=lambda :calculate1()).grid(row=5, column=2)
Button(text='-->', command=lambda: undo1()).grid(row=2, column=3)
Button(text=' / ', command=lambda :get_operator('/')).grid(row=2, column=4)
Button(text=' pi ', command=lambda :get_operator('3.14')).grid(row=2, column=5)
Button(text=' * ', command=lambda :get_operator('*')).grid(row=3, column=3)
Button(text=' ( ', command=lambda :get_operator('(')).grid(row=3, column=4)
Button(text=' ) ', command=lambda :get_operator(')')).grid(row=3, column=5)
Button(text=' - ', command=lambda :get_operator('-')).grid(row=4, column=3)
Button(text=' % ', command=lambda :get_operator('%')).grid(row=4, column=4)
Button(text='exp', command=lambda :get_operator('**')).grid(row=4, column=5)
Button(text=' + ', command=lambda :get_operator('+')).grid(row=5, column=3)
Button(text='X! ').grid(row=5, column=4)
Button(text='^2 ', command=lambda :get_operator('**2')).grid(row=5, column=5)

root.mainloop()
