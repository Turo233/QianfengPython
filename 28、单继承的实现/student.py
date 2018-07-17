from person import Person

class Student(Person):
    def __init__(self, name, age, money):
        #调用父类中的__init__
        super(Student, self).__init__(name, age, money)
        #子类可以有一些自己督邮的属性


    #子类也可以有自己的独有方法
    def setFunc(self):
        print(self.__money)
