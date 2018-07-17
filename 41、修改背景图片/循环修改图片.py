import win32api
import win32con
import win32gui
import time
import os

def setWallPaper(path):
    #打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop", 0 ,
                                    win32con.KEY_SET_VALUE)
    #2拉伸  0 居中  6 适应  10 填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0,
                          win32con.REG_SZ, "6")
    # win32api.RegSetValueEx(reg_key, )
    # win32api.RegSetValueEx(reg_key, "WallPaper")
    # SPIF_SENDWININICHANGE 立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                path,
                win32con.SPIF_SENDWININICHANGE)

def travFile(path):
    pathFile = os.listdir(path)
    absPathList = []
    for fileName in pathFile:
        absPath = os.path.join(path, fileName)
        # print(absPath)
        if os.path.splitext(absPath)[1] == ".jpg":
            # print(absPath)
            absPathList.append(absPath)
    return absPathList


def changeBG(jpgList):
    for eachJpg in jpgList:
        setWallPaper(eachJpg)
        time.sleep(3)



jpgPath = r"F:\jpg"
filePath = travFile(jpgPath)
changeBG(filePath)
