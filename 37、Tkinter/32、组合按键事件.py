import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

# <Control-Alt-a>
# <Shift-Up>

def func(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("<Shift-Up>", func)


win.mainloop()
