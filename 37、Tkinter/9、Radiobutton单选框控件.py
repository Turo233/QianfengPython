import tkinter

def update():
    print(r.get())

win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")


#一组单选框要绑定同一个变量
r = tkinter.IntVar()

radio1 = tkinter.Radiobutton(win, text="one",
                            value=11,
                            variable=r,
                            command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two",
                            value=2,
                            variable=r,
                            command=update)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="one",
                            value=3,
                            variable=r,
                            command=update)
radio3.pack()


win.mainloop()
