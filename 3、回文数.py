num = 10000
sum = 0
while num < 100000:
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    d = (num // 1000) % 10
    e = (num // 10000) % 10
    if (a == e and b == d):
        print("num = %d 是回文数" % num)
        sum += 1
    num += 1
print("共有 %d 个" % sum)
