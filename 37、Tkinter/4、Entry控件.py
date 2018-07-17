import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

'''
Entry: 输入控件，用于显示简单的文本内容
'''

#绑定变量
e = tkinter.Variable()

entry = tkinter.Entry(win, textvariable=e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("turo is a good man")

#取值
# print(e.get())
# print(entry.get())

#show  密文显示
entry1 = tkinter.Entry(win, show="*")
entry1.pack()



win.mainloop()
