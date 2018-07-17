import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

'''
Entry: 输入控件，用于显示简单的文本内容
'''



entry = tkinter.Entry(win)
entry.pack()


button = tkinter.Button(win, text="按钮", command=lambda: print(entry.get()),
                        width=10, height=1)
button.pack()




win.mainloop()
