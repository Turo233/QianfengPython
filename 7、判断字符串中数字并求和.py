text = input("请输入需要判断的字符串：")
i = 0
sum = 0
while i < len(text):
    if ord(text[i]) > 48 and ord(text[i]) < 57:
        sum += int(text[i])
    i += 1
print("字符串中数字的和为 %d " % sum)


# print(ord('0')) = 48
# print(ord('9')) = 57
