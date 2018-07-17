import tkinter
import os
from tkinter import ttk


class treeWindows(tkinter.Frame):
    #直接在init中添加otherWin参数，可在本类中直接对otherWin中内容进行操作
    def __init__(self, master, path, otherWin):
        self.otherWin = otherWin
        #在master上创建frame框架
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        #创建树
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT)

        #创建根目录
        fileName = self.filePathName(path)

        self.root = self.tree.insert("", "end", text=fileName, values=([path]))#猜想元组会将重复的"\"自动过滤，所以将地址放入列表中，实现其地址的传递
        self.loadTree(self.root, path)

        #创建滚动条
        sc = tkinter.Scrollbar(frame)
        sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        sc.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=sc.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)


    def func(self, event):
        #提取名字
        self.otherWin.txt.delete(0.0, tkinter.END)
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            # entry模块不能直接insert插入内容，需要绑定变量，而绑定变量需要在其类中添加
            self.otherWin.ev.set(file)
            # print(file)
            apath = self.tree.item(sv)["values"][0]
            if os.path.splitext(apath)[1] == ".py":
                with open(apath, "r", encoding="utf-8", errors=None) as f:
                    self.otherWin.txt.insert(tkinter.INSERT, f.read())




    def loadTree(self, parent, path):
        for fileName in os.listdir(path):
            absPath = os.path.join(path, fileName)
            print(absPath)
            # 插入树枝
            newFileName = self.filePathName(absPath)
            treey = self.tree.insert(parent, "end", text=newFileName, values=([absPath]))

            # 判断树枝是否为目录、如果是，遍历自己
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath)



    #创建一个可以弄出路径最后名称的方法
    def filePathName(self, path):
        return os.path.split(path)[-1]
