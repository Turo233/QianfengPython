import csv
import sys
import importlib
importlib.reload(sys)
import win32com
import win32com.client

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed



class dealFile(object):
    #读取csv
    def readCsv(self, path):
        infoList = []
        with open(path, "r") as f:
            allFileInfo = csv.reader(f)
            print(allFileInfo)
            for row in allFileInfo:
                infoList.append(row)
        return infoList
    # 写csv，data格式特殊要求
    def writeCsv(self, path, data):
        with open(path, "w") as f:
            writer = csv.writer(f)
            for rowData in data:
                print("rowData = ", rowData)
                writer.writerow(rowData)
    #pdf
    def readPDF(self, path, callback=None, toPath=""):
        #以二进制形式打开pdf文件
        f = open(path, "rb")
        #创建一个pdf文档分析器
        parser = PDFParser(f)

        #创建一个pdf文档
        pdfFile = PDFDocument()

        #链接-》分析器和创建文档对象-》双向链接
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        #提供初始化密码
        pdfFile.initialize()

        #检测文档是否提供txt转换
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            #解析数据

            #数据管理器
            manager = PDFResourceManager()

            #创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)

            #创建解释器对象
            interpreter = PDFPageInterpreter(manager, device)


            #开始循环处理， 每次处理一页
            for page in pdfFile.get_pages():
                interpreter.process_page(page)

                layout = device.get_result()
                for x in layout:
                    #判断x是否为LTTextBoxHorizontal类型，是才能处理
                    if (isinstance(x, LTTextBoxHorizontal)):
                        if toPath == "":
                            #处理每行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)#为了避免每次处理str都要修改类，所以添加此方法
                            # print(str)
                        else:
                            print(str)

            f.close()
    #word
    def readWordFile(path):
        #调用系统word功能，可以处理doc和docx两种文件
        mw = win32com.client.Dispatch("Word.Application")
        #打卡文件
        # print(type(mw))
        doc = mw.Documents.Open(path)
        # print(type(doc))
        for paragraph in doc.Documents:
            line = paragraph.Range.Text
            print(line)#也可以回调
        #关闭文件
        doc.Close()
        #退出word
        mw.Quit()
