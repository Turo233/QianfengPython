import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")



# <Enter>鼠标进入控件时触发
# <Leave>鼠标离开控件时触发
label1 = tkinter.Label(win, text="turo is a good man", bg="red")
label1.pack()

def func(event):
    print(event.x, event.y)
label1.bind("<Leave>", func)

win.mainloop()
