from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ''
    text_Input.set(operator)


def btnDeleteDisplay():
    global operator
    operator = str(operator[0:-1])
    text_Input.set(operator)


def btnEqualsInput():
    try:
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ''

    except ZeroDivisionError:
        text_Input.set('Error')



cal = Tk()
cal.title('Калькулятор')
operator = ''
text_Input = StringVar()
cal.eval('tk::PlaceWindow %s center' % cal.winfo_pathname(cal.winfo_id()))

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=45, insertwidth=5,
                   bg='tomato', justify='right').grid(columnspan=4)
btn7 = Button(cal,  padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='7', bg='tomato', command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='8', bg='tomato', command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='9', bg='tomato', command=lambda: btnClick(9)).grid(row=1, column=2)
Addition = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='+', bg='tomato', command=lambda: btnClick('+')).grid(row=1, column=3)
# Next row
btn4 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='4', bg='tomato', command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='5', bg='tomato', command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='6', bg='tomato', command=lambda: btnClick(6)).grid(row=2, column=2)
Subtraction = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='-', bg='tomato', command=lambda: btnClick('-')).grid(row=2, column=3)
# Next row
btn1 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='1', bg='tomato', command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='2', bg='tomato', command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='3', bg='tomato', command=lambda: btnClick(3)).grid(row=3, column=2)
Multiply = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='*', bg='tomato', command=lambda: btnClick('*')).grid(row=3, column=3)
# Next row
btn0 = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='0', bg='tomato', command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='C', bg='tomato', command=btnClearDisplay).grid(row=4, column=1)
btnd = Button(cal, padx=22, pady=20, bd=5, fg='black', font=('arial', 20, 'bold'),
              text='<', bg='tomato', command=btnDeleteDisplay).grid(row=4, column=2)
Divison = Button(cal, padx=22, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='/', bg='tomato', command=lambda: btnClick('/')).grid(row=4, column=3)
# Next row
btnEquals = Button(cal, padx=170, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='=', bg='tomato', command=btnEqualsInput).grid(row=5, columnspan=4)

cal.mainloop()