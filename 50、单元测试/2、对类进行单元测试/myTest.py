import unittest
from person import Person

class test(unittest.TestCase):
    def test_init(self):
        p = Person("Jack", 18)
        self.assertEqual(p.name, "Jack", "属性赋值错误")

    def test_getAge(self):
        p = Person("Jack", 18)
        self.assertEqual(p.getAge(), p.age, "getAge函数有误")


if __name__ == "__main__":
    unittest.main()
