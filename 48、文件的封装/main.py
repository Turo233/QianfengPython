from dealFile import dealFile

d = dealFile()

path = r"E:\1编程\千锋python\Code\48、文件的封装\turo.pdf"



def func(str):
    print(str + "!")

#               回调函数，在另一个函数里执行了这个函数
d.readPDF(path, func)
