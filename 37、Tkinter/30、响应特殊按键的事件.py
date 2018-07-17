#shift/ctrl/...


import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

# <Shift_L>左shift
# <Shift_R>右shift
# <F5>
# <Return>   回车
# <BackSpace>


label1 = tkinter.Label(win, text="turo is a good man", bg="red")
# label1.focus_set()
label1.pack()

def func(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("<Shift_L>", func)


win.mainloop()
