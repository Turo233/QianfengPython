import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    mw = win32com.client.Dispatch("Word.Application")

    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件
    doc.SaveAs(toPath, 2) #2表示为txt文件
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

toPath = r"‪E:\1编程\千锋python\Code\45、读取word\a.txt"
path = r"‪E:\论文\林\中、英文摘要（含关键词）.doc"
readWordFileToOtherFile(path, toPath)
