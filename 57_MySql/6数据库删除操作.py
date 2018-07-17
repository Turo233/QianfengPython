import pymysql

db = pymysql.connect("192.168.5.102", "root", "turo", "turo233")
cursor = db.cursor()


sql = 'delete from bankcard where money=200'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败, 回滚到上一次的数据
    db.rollback()

cursor.close()
db.close()
