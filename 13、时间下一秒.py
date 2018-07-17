timeDate = input("输入时间：")
timeList = timeDate.split(":")

s = int(timeList[2])

m = int(timeList[1])

h = int(timeList[0])

s += 1

if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0

print("%.2d:%.2d:%.2d" % (h, m, s))
