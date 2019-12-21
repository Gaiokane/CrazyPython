class Tiger1:
    #类方法两点：A、用@classmethod修饰。B、定义一个cls形参
    @classmethod
    def info(cls):
        print('info类方法')
        print(cls)

print(Tiger1)
#类方法属于类本身，因此用类来调用
#类方法第一个cls参数也会自动绑定，绑定到调用该方法的类
Tiger1.info()

t = Tiger1()
#对象调用类方法，实际上也相当于用类调用类方法，同样也会执行自动绑定
#第一个参数绑定当前类
t.info()

print('-' * 50)

class Tiger2:
    #静态方法两点：A、用@staticmethod修饰。B、无需定义任何形参
    @staticmethod
    def info(p):
        print('info静态方法')
        print(p)

#静态方法相当于一个函数，因此不会自动绑定
#类调用用静态方法，因此必须为参数传入参数值
Tiger2.info('qqq')

t = Tiger2()
#对象调用静态方法，也不会自动绑定，因此必须为参数传入参数值
t.info(t)

'''
            实例方法        类方法      静态方法
对象调用    自动绑定        自动绑定    不自动绑定
类调用      不自动绑定      自动绑定    不自动绑定
'''