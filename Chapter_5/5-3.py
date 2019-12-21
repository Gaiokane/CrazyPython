class User:
    def __init__(self, name='tiger'):
        #self代表该构造器正在构造的对象
        self.name = name
    
    def info(self):
        print(self)
        print(self.name)

#User构造的对象，赋值给u，在User构造器中的self实际上就代表u
u = User()
print(u.name)

#User构造的对象，赋值给u2，在User构造器中的self实际上就代表u2
u2 = User('scott')
print(u2.name)

print(u2)

#-----实例方法第一个self不需要传入，由系统自动绑定，总是绑定到方法调用者-----
#-----方法中的self总是代表该方法的调用者-----

#程序用u2调用info方法，那么info中的self就代表u2
u2.info()

#程序用u1调用info方法，那么info中的self就代表u2
u.info()

print('-' * 50)

class Dog:
    def run(self):
        #一个方法调用其他方法，也需要使用self来调用
        self.jump()
        print('狗在跑')

    def jump(self):
        print('狗要跳')

d = Dog()
d.run()

print('-' * 50)

class Planet:
    def __init__(self, height=2):
        self.height = 2
    
    def grow(self):
        #每grow一次，height增加10
        self.height += 10
        return self

p = Planet()
print(p.height)
p.grow()
print(p.height)
#如果grow方法return self——self本身又代表方法调用者：p
p.grow().grow().grow()
print(p.height)

print('-' * 50)

class Role:
    def test(self):
        print('test方法')

#test方法本身是实例方法，应该用对象调用
#但python允许用类调用实例方法，此时就变成了”未绑定的方法“，因此必须显式为self参数传入参数值
r = Role()
Role.test(r)