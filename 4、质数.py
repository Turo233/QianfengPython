num = int(input("请输入一个数来判断是否为质数："))
i = 2
# count = 0
if num == 2:
    print("是质数")
else:
    while i <= num - 1:
        if num % i == 0:
            print("不是质数")
            # count += 1
            break
        i += 1
    # if not count:
        # print("是质数")
    if i == num:
        print("是质数")
