from tkinter import *
from tkinter.messagebox import *
import math as m
#some useful variables
font = ('Verdana', 22, 'bold')

#functionality
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    b = event.widget
    text = b["text"]

    if text == 'X':
        textField.insert(END, '*')
        return

    if text == '=':
        try:
            ex = textField.get()
            ans = eval(ex)
            textField.delete(0, END)
            textField.insert(0, ans)
            return
        except Exception as e:
            print('Error..', e)
            showerror('Error', e)
            return
    if text == '<---':
        return
    if text == 'AC':
        return
    else:
        textField.insert(END, text)

def enterClick(event):
    e = Event()
    e.widget = eqbtn
    click_btn_function(e)

#creating a window
window = Tk()
window.title('My Calculator')
window.geometry('400x470')

#picture label
pic = PhotoImage(file = 'calculator.png')
headingLabel = Label(window, image = pic)
headingLabel.pack(side = TOP, pady = 10)

#heading label
heading = Label(window, text = 'My Calculator', font = font)
heading.pack(side = TOP)

#textfield
textField = Entry(window, font = font, justify = CENTER, relief = 'solid')
textField.pack(side = TOP, pady = 10, padx = 10, fill = X)

#buttons
buttonFrame = Frame(window)
buttonFrame.pack(side = TOP)

#adding button
count = 1
for i in range(3):
    for j in range(3):
        btn = Button(buttonFrame, text = str(count), font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
        btn.grid(row = i, column = j, padx = 3, pady = 3)
        count += 1
        btn.bind('<Button-1>', click_btn_function)

zerobtn = Button(buttonFrame, text = '0', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
zerobtn.grid(row = 3, column = 0, padx = 3, pady = 3)

dotbtn = Button(buttonFrame, text = '.', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
dotbtn.grid(row = 3, column = 1, padx = 3, pady = 3)

eqbtn = Button(buttonFrame, text = '=', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
eqbtn.grid(row = 3, column = 2, padx = 3, pady = 3)

plusbtn = Button(buttonFrame, text = '+', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
plusbtn.grid(row = 0, column = 3, padx = 3, pady = 3)

minusbtn = Button(buttonFrame, text = '-', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
minusbtn.grid(row = 1, column = 3, padx = 3, pady = 3)

multbtn = Button(buttonFrame, text = 'X', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
multbtn.grid(row = 2, column = 3, padx = 3, pady = 3)

divbtn = Button(buttonFrame, text = '/', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
divbtn.grid(row = 3, column = 3, padx = 3, pady = 3)

clrbtn = Button(buttonFrame, text = '<---', font = font, width = 8, relief = 'solid', activebackground = 'orange', activeforeground = 'white', command = clear)
clrbtn.grid(row = 4, column = 0, padx = 3, pady = 3, columnspan = 2)

allclrbtn = Button(buttonFrame, text = 'AC', font = font, width = 8, relief = 'solid', activebackground = 'orange', activeforeground = 'white', command = all_clear)
allclrbtn.grid(row = 4, column = 2, padx = 3, pady = 3, columnspan = 2)

eqbtn.bind('<Button-1>', click_btn_function)
plusbtn.bind('<Button-1>', click_btn_function)
minusbtn.bind('<Button-1>', click_btn_function)
multbtn.bind('<Button-1>', click_btn_function)
divbtn.bind('<Button-1>', click_btn_function)
clrbtn.bind('<Button-1>', click_btn_function)
allclrbtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
dotbtn.bind('<Button-1>', click_btn_function)
textField.bind('<Return>', enterClick)

#Scientific Calculator
scFrame = Frame(window)
sqrtbtn = Button(scFrame, text = '√', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
sqrtbtn.grid(row = 0, column = 0, padx = 3, pady = 3)

powbtn = Button(scFrame, text = '^', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
powbtn.grid(row = 0, column = 1, padx = 3, pady = 3)

facbtn = Button(scFrame, text = 'x!', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
facbtn.grid(row = 0, column = 2, padx = 3, pady = 3)

radbtn = Button(scFrame, text = 'toRad', font = font, width = 5, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
radbtn.grid(row = 0, column = 3, padx = 3, pady = 3)

degbtn = Button(scFrame, text = 'toDeg', font = font, width = 5, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
degbtn.grid(row = 1, column = 3, padx = 3, pady = 3)

sinbtn = Button(scFrame, text = 'sinΘ', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
sinbtn.grid(row = 1, column = 0, padx = 3, pady = 3)

cosbtn = Button(scFrame, text = 'cosΘ', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
cosbtn.grid(row = 1, column = 1, padx = 3, pady = 3)

tanbtn = Button(scFrame, text = 'tanΘ', font = font, width = 3, relief = 'solid', activebackground = 'orange', activeforeground = 'white')
tanbtn.grid(row = 1, column = 2, padx = 3, pady = 3)

normal_calc = True

def calculate_sc(event):
    btn = event.widget
    text = btn['text']

    ans = ''
    ex = textField.get()
    if text == 'toDeg':
        ans = str(m.degrees(float(ex)))
        textField.delete(0, END)

    if text == 'toRad':
        ans = str(m.radians(float(ex)))
        textField.delete(0, END)

    elif text == 'x!':
        ans = str(m.factorial(int(ex)))
        textField.delete(0, END)

    elif text == 'sinΘ':
        ans = str(m.sin(m.radians(float(ex))))
        textField.delete(0, END)

    elif text == 'cosΘ':
        ans = str(m.cos(m.radians(float(ex))))
        textField.delete(0, END)

    elif text == 'tanΘ':
        ans = str(m.tan(m.radians(float(ex))))
        textField.delete(0, END)

    elif text == '√':
        ans = str(m.sqrt(float(ex)))
        textField.delete(0, END)

    elif text == '^':
        ex = textField.get()
        li = ex.split(',')
        ans = str(float(li[0]) ** int(li[1]))
        textField.delete(0, END)

    textField.insert(0, ans)

def sc_click():
    global normal_calc
    if normal_calc is True:
        buttonFrame.pack_forget()
        scFrame.pack(side = TOP)
        buttonFrame.pack(side = TOP)
        window.geometry('500x600')
        normal_calc = False
    else:
        scFrame.pack_forget()
        buttonFrame.pack_forget()
        buttonFrame.pack(side = TOP)
        window.geometry('400x470')
        normal_calc = True

sqrtbtn.bind('<Button-1>', calculate_sc)
powbtn.bind('<Button-1>', calculate_sc)
facbtn.bind('<Button-1>', calculate_sc)
radbtn.bind('<Button-1>', calculate_sc)
degbtn.bind('<Button-1>', calculate_sc)
sinbtn.bind('<Button-1>', calculate_sc)
cosbtn.bind('<Button-1>', calculate_sc)
tanbtn.bind('<Button-1>', calculate_sc)

######################


fontMenu = ('', 10)
menubar = Menu(window, font = fontMenu)
mode = Menu(menubar, font = fontMenu, tearoff = 0)
mode.add_checkbutton(label = 'Scientific Calculator', command = sc_click)
menubar.add_cascade(label = 'Mode', menu = mode)

window.config(menu = menubar)
window.mainloop()