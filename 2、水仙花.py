num = 100
while num <= 1000:
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    if num == (a**3 + b**3 + c**3):
        print("num = %d 是水仙花数" % num)
    num += 1
