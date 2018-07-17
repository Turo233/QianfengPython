class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def run(self):
        print("run")

    def eat(self, food):
        print("ear " + food)
