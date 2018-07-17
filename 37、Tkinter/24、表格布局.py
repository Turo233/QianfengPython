import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="yellow")
label4 = tkinter.Label(win, text="handsome", bg="black")

#表格布局

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

win.mainloop()
