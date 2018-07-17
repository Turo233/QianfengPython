import tkinter

def update():
    message=""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    #清楚text中所有的内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)

win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

#要绑定的变量
hobby1 = tkinter.BooleanVar()
#多选框
check1 = tkinter.Checkbutton(win, text="money",
                             variable=hobby1,
                             command=update)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="power",
                             variable=hobby2,
                             command=update)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="people",
                             variable=hobby3,
                             command=update)
check3.pack()

#怎么知道选择了几个->绑定变量

text = tkinter.Text(win, width=50, height=10)
text.pack()

win.mainloop()
