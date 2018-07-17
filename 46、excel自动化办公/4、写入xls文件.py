#有序字典
from collections import OrderedDict
#存储数据
from pyexcel_xls import save_data




def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path, dic)

path = r"E:\1编程\千锋python\Code\46、excel自动化办公\a.xls"
#数据格式很固定
makeExcelFile(path, {"表1":[[1, 2, 3], [3, 4, 5], [4, 5 ,6]],
                     "表2":[[11, 1, 23], [23, 43, 51], [34, 45, 16]]})
