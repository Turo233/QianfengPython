import tkinter


def func():
    print("turo is a good man")

win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

'''
Button:按钮
'''

button = tkinter.Button(win, text="按钮", command=func,
                        width=10, height=1)
button.pack()
button1 = tkinter.Button(win, text="按钮", command=win.quit,
                        width=10, height=1)
button1.pack()
win.mainloop()
