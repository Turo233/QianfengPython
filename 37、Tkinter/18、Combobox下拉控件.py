import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")


#绑定变量使get()全部生效
cv = tkinter.StringVar()

com = ttk.Combobox(win, textvariable=cv)
com.pack()
#设置下拉数据
com["value"] = ("黑龙江", "吉林", "辽宁")

#设置默认值,index
com.current(0)

#绑定事件<<ComboboxSelected>>
def func(event):
    print(com.get())
    print(cv.get())
com.bind("<<ComboboxSelected>>", func)


win.mainloop()
