while True:
    print("*"*50)
    print("请输入N A B 以空格分隔:")
    N, A, B = map(int, input().split())
    if not (N >= 1 and N <= 20):
        continue
    if not (A >= 1 and A <= 100):
        continue
    if not (B >= 1 and B <= 2000):
        continue
    break

a_fee = N * A
b_fee = B

min_fee = a_fee if a_fee < b_fee else b_fee

print("*"*50)
print(min_fee)
if a_fee != b_fee:
    print("~ If you choose Plan 1, the fee will be %d x %d = %d yen." % (N, A, a_fee))
    print("~ if you choose plan 2, the fee will be %d yen." % (b_fee))

    print("Thus, the minimum fee is %d yen." % min_fee)
else:
    print("The fee might be the same in the two plans")
