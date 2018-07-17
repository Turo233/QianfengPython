import win32con
import win32gui
import time

#找出窗体的编号
#QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
#                                类名          标题
#显示窗体
#win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
#time.sleep(1)
#隐藏窗体
#win32gui.ShowWindow(QQWin, win32con.SW_HIDE)

while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(1)
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(1)
