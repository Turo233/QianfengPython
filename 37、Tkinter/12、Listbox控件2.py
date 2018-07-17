import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("+400+100")

#EXTENDED 可以使Listbox支持shift和ctrl

lb = tkinter.Listbox(win,
                     selectmode=tkinter.EXTENDED)


for item in ["good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn",
            "good", "nice", "handsome", "cool", "vg", "vn"]:
    lb.insert(tkinter.END, item)

#shift连选
#ctrl跳选

#滚动条
scroll = tkinter.Scrollbar(win)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=scroll.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
scroll["command"] = lb.yview



win.mainloop()
