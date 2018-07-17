import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")


def func(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("a", func)


win.mainloop()
