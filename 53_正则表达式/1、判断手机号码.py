import re
'''
需求:给你一串字符串,判断这是否是手机号码

'''

def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39" and str[1:3] != "31":
        return False
    else:
        for eachN in str[3:]:
            if eachN < "0" or eachN > "9":
                return False
    return True
def checkPhone2(str):
    #13912345678
    pat = r"(1(([3578]\d)|4(7))\d{8})"
    res = re.findall(pat, str)
    return res
# print(checkPhone("13912345678"))
# print(checkPhone("139123456783"))
# print(checkPhone("1391234a378"))
# print(checkPhone("23912345678"))
# print(checkPhone("19012345678"))
'''
print(checkPhone2("13912345678"))
print(checkPhone2("139123456783"))
print(checkPhone2("1391234a378"))
print(checkPhone2("23912345678"))
print(checkPhone2("19012345678"))
print(checkPhone2("14712345678"))
'''

checkPhone2("asfadf13712345678adsfkasf13512345678sfa")
