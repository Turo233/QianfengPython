from Father import Father
from Mother import Mother

class Child(Father, Mother):
    def __init__(self, money, faceValue):
        #写法
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
