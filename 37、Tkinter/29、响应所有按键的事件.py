import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")



'''
# <Key> 响应所有的按键
label1 = tkinter.Label(win, text="turo is a good man", bg="red")
#给小控件设置焦点，才能响应
label1.focus_set()
label1.pack()

def func(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
label1.bind("<Key>", func)
'''
#win不用设置焦点也能响应
def func(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("<Key>", func)



win.mainloop()
