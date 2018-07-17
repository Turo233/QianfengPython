from person import Person
from student import Student

stu = Student("tom", 19, 1234)
far = Person("jack", 39, 123134)

print(stu.name, stu.age)

#print(stu.__money) 私有属性
#stu.setFunc()
print(stu.getMoney())#通过集成过来的共有方法访问私有属性
print(far.getMoney())
