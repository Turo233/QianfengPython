from Child import Child


def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    c.func()
    #注意：父类中方法名相同，默认调用的括号中排前面的父类中的方法
if __name__ == "__main__":
    main()
