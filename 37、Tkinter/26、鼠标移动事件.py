import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")


# <B1-Motion>左键移动
# <B2-Motion>中键移动
# <B3-Motion>右键移动

label1 = tkinter.Label(win, text="turo is a good man")
label1.pack()

def func(event):
    print(event.x, event.y)
label1.bind("<B1-Motion>", func)




win.mainloop()
