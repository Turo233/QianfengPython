import random


for i in range(6):
    ranAlp = chr(random.randint(97, 122))
    ranalp = chr(random.randint(65, 90))
    ranNum = random.randint(0, 10)
    veriCode = random.choice([ranalp, ranalp, ranNum])
    print(veriCode, end="")
