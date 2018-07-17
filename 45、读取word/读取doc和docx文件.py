import win32com
import win32com.client

def readWordFile(path):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打卡文件
    # print(type(mw))
    doc = mw.Documents.Open(path)
    # print(type(doc))
    for paragraph in doc.Documents:
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()
path = r"‪E:\论文\林\中、英文摘要（含关键词）.doc"
readWordFile(path)
