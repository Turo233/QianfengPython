import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

#MULTIPLE 支持多选
lb = tkinter.Listbox(win,
                     selectmode=tkinter.MULTIPLE)

for item in ["good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn"]:
    lb.insert(tkinter.END, item)
lb.pack()

win.mainloop()
