import tkinter
import os
from tkinter import ttk
from treeWindow import treeWindows
from infoWindows import InfoWindows



win = tkinter.Tk()
win.title("Turo")
win.geometry("800x400+400+100")


path = r"E:\1编程"
infoWin = InfoWindows(win)
treeWin = treeWindows(win, path, infoWin)





win.mainloop()
