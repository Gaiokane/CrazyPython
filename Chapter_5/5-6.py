class User:
    #类空间中定义的变量，是类变量
    category = '未知类型'
    def __init__(self, name='admin', passwd='pwd'):
        #通过self引用赋值的变量，是实例变量
        self.name = name
        self.passwd = passwd

#通过类引用赋值的变量，类变量
User.type = '通用用户'

print(User.category)
User.category = '改变后的类型'
print(User.category)

us = User()
#当对象本身没有category实例变量时，对象可访问该类变量
print(us.category)

#只要通过对象对变量赋值，就变成了新增实例变量
us.category = '实例类型'
#当对象本身已有category实例变量时，对象优先访问实例变量
print(us.category)
print(User.category)#此处依然是访问类变量

print('-' * 50)

#————————————————————————————————————————————————————————————————

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getarea(self):
        print('getarea方法')
        return self.width * self.height

    #合成了一个计算面积的属性
    area = property(fget=getarea, doc='获取面积的属性')

    def getsize(self):
        print('getsize方法')
        return self.width, self.height
    def setsize(self, size):
        print('setsize方法')
        self.width = size[0]
        self.height = size[1]
    
    #合成了一个代表大小的属性
    size = property(fget=getsize, fset=setsize, doc='代表大小的属性')

r = Rectangle(30 ,40)
#访问area属性（实际上就是调用getter方法）
print(r.area)

#访问size属性（实际上就是调用getter方法）
print(r.size)

#对size属性赋值（实际上就是调用setter方法）
r.size = (5, 6)
print(r.area)

print('-' * 50)

#————————————————————————————————————————————————————————————————

class Rectangle_property:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #装饰器合成一个只读属性，此时只读属性名与方法名相同
    @property
    def area(self):
        print('getarea方法')
        return self.width * self.height
    
    @property#默认是只读属性
    def size(self):
        print('getsize方法')
        return self.width, self.height
    @size.setter
    def size(self, size):
        print('setsize方法')
        self.width = size[0]
        self.height = size[1]

rp = Rectangle_property(30 ,40)
#访问area属性（实际上就是调用getter方法）
print(rp.area)

#访问size属性（实际上就是调用getter方法）
print(rp.size)

#对size属性赋值（实际上就是调用setter方法）
rp.size = (5, 6)
print(rp.area)