from pymongo import MongoClient


#连接服务器
conn = MongoClient("localhost", 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#添加文档
collection.insert([{"name":"lilei", "age": 19, "gender":1, "address": "北京", "isDelete": 0},
{"name": "张三", "age": 13, "gender": 1, "address": "邯郸", "isDelete": 0}])



#断开
conn.close()
