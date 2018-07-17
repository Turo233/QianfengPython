import sys
import importlib
importlib.reload(sys)


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def readPDF(path, toPath):
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
                    with open(toPath, "a") as f:
                        str = x.get_text()
                        #处理数据
                        print(str)
                        f.write(str+"\n")









#出现\u202错误 手动打路径可解决
path = r"E:\1编程\千锋python\Code\39、读写pdf文件\turo.pdf"
toPath = r"E:\1编程\千锋python\Code\39、读写pdf文件\a.txt"
readPDF(path, toPath)
