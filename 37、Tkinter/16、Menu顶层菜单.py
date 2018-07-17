import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")



#菜单条
menubar = tkinter.Menu(win)
#配置菜单条放到menu上
win.config(menu=menubar)

def func():
    print("turo is a good man")

#创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
#给菜单选项添加内容
for item in ["Python", "C", "C++", "OC", "Swift",
            "c#", "shell", "Java", "JS", "PHP",
            "汇编", "NodeJS", "退出"]:
    if item == "退出":
        #添加分割线
        menu1.add_separator()

        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)

#向菜单条上添加选项
menubar.add_cascade(label="语言", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")
menubar.add_cascade(label="颜色", menu=menu2)
win.mainloop()
