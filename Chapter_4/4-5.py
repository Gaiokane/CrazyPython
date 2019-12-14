#全局变量
a = 35

def info():
    #局部变量
    b = 'qk'
    #局部变量只能在当前函数内访问
    print(b)
    #全局变量，可在任意函数内访问
    print(a)
    #局部变量组成的数组
    print(locals())

def bar():
    #局部变量
    c = 'qkk'
    #print(b)#错误
    #全局变量，可在任意函数内访问
    print(a)
    #局部变量组成的数组
    print(locals())

#访问全局变量的字典
print(globals())
print('-' * 50)
#locals是获取当前范围的所有局部变量
#因此如果你在全局范围调用locals()，它返回全部的全局变量
#在全局范围内，用globals()和locals()（在全局范围内，它的当前范围就是全局）效果是一样的
print(locals())
print('-' * 50)
info()
print('-' * 50)
bar()
print('-' * 50)

name = 'qk'

def info1():
    #依然访问全局变量name
    print(globals()['name'])
    #在函数内对变量赋值，变成了定义新的name变量
    name = 'qkk'
    print(name)

info1()
#全局变量name没有改变
print(name)

print('-' * 50)

def info2():
    #该函数中name始终使用全局变量
    global name
    #依然访问全局变量name
    print(name)
    #前面已经声明了name始终使用全局变量
    #因此此处不是重新定义局部变量
    name = 'qkk'
    print(name)

info2()
#全局变量name会被改变
print(name)