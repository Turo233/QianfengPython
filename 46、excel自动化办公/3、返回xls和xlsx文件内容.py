#有序字典
from collections import OrderedDict

#读取数据
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = r"E:\1编程\千锋python\Code\46、excel自动化办公\LaGouDataPython.xlsx"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))
