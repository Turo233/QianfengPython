import tkinter


win = tkinter.Tk()
win.title("Turo")
win.geometry("400x400+400+100")

'''
Text控件: 文本控件, 用于显示多行文本
'''


#height : 显示的行数
text = tkinter.Text(win, width=30,
                    height=1)

text.pack()
str = '''For good measure,
 during the spring and summer,
 drought , heat , hail ,grasshopper
 and other frustrations might
 await the wary grower.
  '''

text.insert(tkinter.INSERT, str)





win.mainloop()
