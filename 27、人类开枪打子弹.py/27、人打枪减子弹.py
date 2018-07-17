#人开枪射击子弹

'''
人
类名:Person
属性:gun
行为:fire

枪
类名:Gun
属性:BulletBox
行为:shoot


弹夹
类名:BulletBox
属性:bulletCount

'''
from gun import Gun
from bulletbox import BulletBox
from person import Person

#弹夹
bulletBox = BulletBox(5)
#枪
gun = Gun(bulletBox)
#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fillBullet(3)
per.fire()
per.fire()
per.fire()
per.fire()
