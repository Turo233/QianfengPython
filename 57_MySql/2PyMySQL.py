import pymysql

#连接数据库
#参数 1 : mysql服务所在主机ip
#参数 2 : 用户名
#参数 3 : 密码
#参数 4 : 要连接的数据库名
db = pymysql.connect("192.168.5.102", "root", "turo", "turo233")

#创建一个cursor对象

cursor = db.cursor()

sql = "select version()"

#执行sql语句
cursor.execute(sql)

#获取返回的信息
data = cursor.fetchone()
print(data)

#断开
cursor.close()
db.close()
