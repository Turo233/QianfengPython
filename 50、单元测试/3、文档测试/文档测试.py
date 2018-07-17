# 文档测试写在程序里
import doctest
#doctest模块可以提前注释中的代码执行
#doctest模块严格按照Python 交互模式的输入提取
def mySum(x, y):
    '''
    get The Sum from x and y
    :param x: firstNum
    :param y: SecondNum
    :return: sum

    example:
    注意有空格
    >>> print(mySum(1, 2))
    3
    '''

    return x + y + 1


print(mySum(1, 2))

#进行文档测试
doctest.testmod()
