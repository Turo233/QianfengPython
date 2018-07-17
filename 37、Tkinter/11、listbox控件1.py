import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

#绑定变量
lbv = tkinter.StringVar()

#SINGLE与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win,
                     selectmode=tkinter.SINGLE,
                     listvariable=lbv)

lb.pack()
for item in ["good", "nice", "handsome", "cool", "vg", "vn"]:
    lb.insert(tkinter.END, item)

#打印当前列表中的选项
print(lbv.get())

#设置选项（元组类型）
lbv.set(("1", "2", "3"))
#绑定事件
def myPrint(event): #event
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>", myPrint) #尖尖号



win.mainloop()
