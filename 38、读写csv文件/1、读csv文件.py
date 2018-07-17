import csv


def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
    return infoList


path = r"C:\Users\Administrator\Desktop\LaGouDataPython.csv"
info = readCsv(path)
print(info[0])
