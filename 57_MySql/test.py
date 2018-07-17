
from turoSql import TuroSql

s = TuroSql("192.168.5.102", "root", "turo", "turo233")

res = s.get_all("select * from bankcard where money>400")
for row in res:
    print("%d-%d" % (row[0], row[1]))
