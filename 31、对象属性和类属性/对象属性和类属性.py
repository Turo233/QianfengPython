class Person(object):
    #这里的属性实际上属于类属性（用类名来调用）
    name = "person"
    def __init__(self, name):
        # 对象属性
        self.name = name


print(Person.name)
per = Person("Tom")
#对象属性的优先级高于类属性
per.name = "aaa" #相当于添加了一个对象属性
print(per.name)
#动态的给对象添加对象属性
per.age = 18#只针对于当前对象生效，对于类创建的其他对象没有作用

print(Person.name)

per2 = Person("lilei")
#print(per2.age)#没有age属性


#删除对象中的name属性,在调用时会使用到同名的类属性
del per.name
print(per.name)
#注意：以后千万不要将对象属性和类属性重名，因为对象属性会屏蔽掉类
#属性。但是当删除对象属性后，在使用又能使用类属性了。
