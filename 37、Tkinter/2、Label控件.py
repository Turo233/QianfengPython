import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

'''
Label : 标签控5件可以显示文本
'''

#win：父窗体
#text:显示的文本内容
#bg: 背景色
#fh:  字体颜色
#wraplength: 指定text文本中多宽进行换行
#justify: 设置换行后的对齐方式
#anchor: 位置n e s w = 北 东 南 西  center(默认) ne se sw nw
label = tkinter.Label(win,
                      text="Turo",
                      bg="blue",
                      fg="white",
                      font=("黑体", 20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="w")
#显示出来
label.pack()




win.mainloop()
