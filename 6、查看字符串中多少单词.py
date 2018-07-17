text = input("请输入需要判断单词的字符串: ")
num = 0
index = 0
#除去开头结尾的空格
str1 = text.strip()
# #单词中有空格不行
# # while i < len(str1):
# #     if str1[i] == " ":
# #         num += 1
# #     i += 1
# # print("有%d个单词" % num)
# while index < len(str1):
#     #跳过单词
#     while str1[index] != " ":
#         index += 1
#         #尾端判断
#         if index == len(str1):
#             num += 1
#             break
#     if index == len(str1):
#         break
#     num += 1
#     #跳过空格
#     while str1[index] == " ":
#         index += 1
#
# print(num)
newText = text.split(" ")
c = 0
for  i in newText:
    if len(i) > 0:
        c += 1
print(c)
