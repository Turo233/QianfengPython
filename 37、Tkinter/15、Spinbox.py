import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

#绑定变量
v = tkinter.StringVar()

'''
数值范围控件
increment 步长，默认为1
values 最好不要与from_ , to, increment同时使用
values=(0,2,4,6,8)
command 只要值改变就会执行对应的方法
'''
def update():
    print(v.get())

sp = tkinter.Spinbox(win, from_=0, to=100,
                     increment=5,
                     textvariable=v,
                     command=update)
sp.pack()
#设置值
v.set(20)
#取值
# print(v.get())


win.mainloop()
