import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="yellow")

#相对布局, 窗体改变对控件有影响
#tkinter.BOTH
label1.pack(fill=tkinter.BOTH, side=tkinter.LEFT)
# label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.place(x=100, y=29)

win.mainloop()
