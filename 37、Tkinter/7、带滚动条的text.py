import tkinter


win = tkinter.Tk()
win.title("Turo")
# win.geometry("400x400+400+100")

#创建滚动条

scroll = tkinter.Scrollbar()

text = tkinter.Text(win, width=50,
                    height=8)
#side放到窗体的哪一侧   fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

#关联
#滚动条控制文本
scroll.config(command=text.yview)
#文本控制滚动条
text.config(yscrollcommand=scroll.set)


str = '''For good measure,
 during the spring and summer,
 drought , heat , hail ,grasshopper
 and other frustrations might
 await the wary grower.
 For good measure,
  during the spring and summer,
  drought , heat , hail ,grasshopper
  and other frustrations might
  await the wary grower.
  For good measure,
   during the spring and summer,
   drought , heat , hail ,grasshopper
   and other frustrations might
   await the wary grower.
   For good measure,
    during the spring and summer,
    drought , heat , hail ,grasshopper
    and other frustrations might
    await the wary grower.
    For good measure,
     during the spring and summer,
     drought , heat , hail ,grasshopper
     and other frustrations might
     await the wary grower.
     For good measure,
      during the spring and summer,
      drought , heat , hail ,grasshopper
      and other frustrations might
      await the wary grower.
  '''

text.insert(tkinter.INSERT, str)





win.mainloop()
