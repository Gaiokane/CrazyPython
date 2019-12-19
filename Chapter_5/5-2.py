class Person:
    def __init__(self, name='qk', age=24):
        print('构造方法')
        self.name = name
        self.age = age

#创建对象时，就是调用构造器
p = Person()
print(p.name, p.age)
print('-' * 50)
p2 = Person('qkk')
print(p2.name, p2.age)
print('-' * 50)
p2 = Person(age=7)
print(p2.name, p2.age)
print('-' * 50)
p2 = Person('Gaiokane', 23)
print(p2.name, p2.age)
print('-' * 50)

class Teacher:
    #空类：只有一个pass语句
    pass

#Teacher没有定义构造器，因此它只有一个只带self参数的构造方法
t = Teacher()

class Item:
    def __init__(self, name='鼠标'):
        self.name = name

im1 = Item('显示器')
print(im1.name)#访问实例变量：显示器
print('-' * 50)

im2 = Item()
print(im2.name)#访问实例变量：鼠标
print('-' * 50)

#改变实例变量的值
im2.name = '键盘'
print(im2.name)
print('-' * 50)

#新增实例变量：对不存在变量赋值即可
im2.color = '黑色'
print(im2.color)
print('-' * 50)

#删除实例变量
del im2.color
#print(im2.color)

def fncolor(self):
    print('fncolor函数')

import types
#为属性赋值，但所赋的值是方法
#该实例变量就变成方法
im2.color = types.MethodType(fncolor, im2)
im2.color()
print('-' * 50)

class Item2:
    #实例方法属于对象，用对象调用
    def test(self):
        print('test方法')

im3 = Item2()
#调用方法
im3.test()
print('-' * 50)

def fn(self):
    print('新增的fn方法')

#增加方法
im3.foo = fn
#新增的方法，默认不会自动绑定self参数
#self参数必须手动传入参数值
im3.foo(im3)
print('-' * 50)
from types import MethodType
#将fn函数包装成方法，且im自动绑定第一个参数
im3.bar = MethodType(fn, im3)
im3.bar()
print('-' * 50)

#可以删除新增的方法
del im3.foo
#im3.foo()