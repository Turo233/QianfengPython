import win32con
import win32gui
import time


QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

#参数1:控制的窗体
#参数2：大致方位, HWND_TOPMOST上方
#参数3：位置x
#参数4：位置y
#参数5：长度
#参数6:宽度


#矩形移动
win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 200, 0,
    600, 400, win32con.SWP_SHOWWINDOW)
x = 200
y = 0
stepX = 1
stepY = 0
while True:
    win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y,
        600, 400, win32con.SWP_SHOWWINDOW)
    x += stepX
    y += stepY

    if x <= 200 and y <= 0:
        stepX = 1
        stepY = 0
    if x >= 500 and y <= 0:
        stepX = 0
        stepY = 1
    if x >= 500 and y >= 300:
        stepX = -1
        stepY = 0
    if x <= 200 and y >= 300:
        stepX = 0
        stepY = -1

#之字形移动
# stepX = 1
# stepY = 0
# while True:
#     win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y,
#     600, 600, win32con.SWP_SHOWWINDOW)
#     x += stepX
#     y += stepY
#     time.sleep(0.005)
#     if x >= 500 and y <= 0:
#         stepX = -1
#     if y <= 0 and x >= 500:
#         stepY = 1
#         stepX = -1
#     if y >= 300 and x <= 200:
#         stepY = 0
#         stepX = 1
#     if y >= 300 and x >= 500:
#         break
