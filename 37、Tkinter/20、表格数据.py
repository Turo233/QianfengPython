import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Turo")
win.geometry("600x400+400+100")

#创建表格
tree = ttk.Treeview(win)
tree.pack()


tree["columns"] = ("姓名", "年龄", "身高", "体重")
#设置列, 列还不显示
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)

#设置表头,text后是显示内容,与上面一一对应
tree.heading("姓名", text="姓名-name")
tree.heading("年龄", text="年龄-age")
tree.heading("身高", text="身高-height")
tree.heading("体重", text="体重-weight")

#添加数据
tree.insert("", 0, text="line0", values=("0", "23", "999", "111"))
tree.insert("", 1, text="line1", values=("1", "23", "999", "111"))
tree.insert("", 2, text="line2", values=("2", "23", "999", "111"))

















win.mainloop()
