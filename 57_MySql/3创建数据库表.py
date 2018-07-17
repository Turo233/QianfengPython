import pymysql

db = pymysql.connect("192.168.5.102", "root", "turo", "turo233")
cursor = db.cursor()

#建表(使用很少)
#检查表是否存在, 如果存在则删除
cursor.execute("drop table if exists bankcard")

#建表
sql = 'create table bankcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)

cursor.close()
db.close()
