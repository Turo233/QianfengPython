import tkinter
import os


class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1)

        self.ev = tkinter.StringVar()
        self.entry = tkinter.Entry(frame, textvariable=self.ev)
        self.entry.pack()



        self.txt = tkinter.Text(frame)
        self.txt.pack(side=tkinter.LEFT)

        sc = tkinter.Scrollbar(frame)
        sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        sc.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=sc.set)
