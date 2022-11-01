from cProfile import label
from tkinter import *
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

root = Tk()
root.title("CALCULATOR",)

e= Entry(root,width=30,fg = "black",bg = "white",borderwidth=5,font = 15)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=15)

def clear():
    e.delete(0,END)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current + str(number)) 

def cal(sign):
    print(sign,type(sign))
    first_number = e.get()
    e.delete(0,END)
    global op 
    op = sign
    global f_num 
    f_num = first_number
    

def equal():
    second_number = e.get()
    e.delete(0,END)
    result = ops[op](int(f_num),int(second_number))
    print("here is the result",result)
    e.insert(0,str(result))

#define buttons
button_1 = Button(root , text ='1',padx =40,pady =20,command=lambda:button_click(1),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_2 = Button(root , text ='2',padx =40,pady =20,command=lambda:button_click(2),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_3 = Button(root , text ='3',padx =40,pady =20,command=lambda:button_click(3),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_4 = Button(root , text ='4',padx =40,pady =20,command=lambda:button_click(4),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_5 = Button(root , text ='5',padx =40,pady =20,command=lambda:button_click(5),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_6 = Button(root , text ='6',padx =40,pady =20,command=lambda:button_click(6),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_7 = Button(root , text ='7',padx =40,pady =20,command=lambda:button_click(7),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_8 = Button(root , text ='8',padx =40,pady =20,command=lambda:button_click(8),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_9 = Button(root , text ='9',padx =40,pady =20,command=lambda:button_click(9),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_0 = Button(root , text ='0',padx =40,pady =20,command=lambda:button_click(0),fg = "white",bg = 'black',font = 20, borderwidth=5)
button_add = Button(root,text="+",padx =40,pady=20,command = lambda :cal('+'),fg = "white",bg="black",font = 20,borderwidth=5)
button_equal = Button(root,text= '=',padx=38,pady=20,command=equal,font = 20,borderwidth=5)
button_clear = Button(root , text='Clear',padx=25,pady=20,command=clear,font = 20,borderwidth=5)


button_subtract = Button(root,text="-",padx =42,pady=20,command = lambda: cal('-'),fg = "white",bg="black",font = 20,borderwidth=5)
button_multiply = Button(root,text="*",padx =41,pady=20,command = lambda:cal('*'),fg = "white",bg="black",font = 20,borderwidth=5)
button_division = Button(root,text="/",padx =41,pady=20,command = lambda:cal('/'),fg = "white",bg="black",font = 20,borderwidth=5)
button_expo = Button(root,text="^",padx =40,pady=20,command = lambda:cal('^'),fg = "white",bg="black",font = 20,borderwidth=5)
button_mod = Button(root,text="%",padx =38,pady=20,command = lambda:cal('%'),fg = "white",bg="black",font =20,borderwidth=5)

#puts buttons on the screen
button_1.grid(row =3 , column=0 )
button_2.grid(row =3, column=1 )
button_3.grid(row =3 , column=2 )

button_4.grid(row =2, column=0 )
button_5.grid(row =2 , column=1 )
button_6.grid(row =2 , column=2 )

button_7.grid(row =1 , column=0 )
button_8.grid(row =1 , column=1 )
button_9.grid(row =1 , column=2 )

button_0.grid(row =4 , column=0 )
button_clear.grid(row = 6, column = 1,columnspan=1)
button_add.grid(row = 5, column =0,columnspan=1)
button_equal.grid(row =6 ,column = 2 ,columnspan=1)
button_subtract.grid(row =4,column =1, columnspan=1)
button_multiply.grid(row = 4 ,column = 2 ,columnspan=1 )
button_division.grid(row = 5, column =2,columnspan=1 )
button_expo.grid(row = 6,column = 0,columnspan=1)
button_mod.grid(row = 5 , column = 1,columnspan=1)


root.mainloop()