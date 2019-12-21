#foo函数，该函数将打算作为函数装饰器使用
#作为函数装饰器使用的函数，它必须定义一个形参
def foo(fn):
    print('foo函数')
    print(fn)
    return 'qqq'

#被装饰的函数
@foo
def bar():
    print('bar函数')

'''
函数装饰器的本质：
（1）将被装饰的函数（bar）作为参数传给装饰器函数（foo）
（2）被装饰的函数（bar）将被替换成装饰器函数（foo）的返回值
'''

print(bar)
#bar被装饰——被替换成装饰器的返回值：qqq
#由于bar其实已经呗替换成了qqq，因此bar函数不能被调用
#bar()

print('-' * 50)
#——————————————————————————————————————————————————————————————————

#foo函数，该函数将打算作为函数装饰器使用
#作为函数装饰器使用的函数，它必须定义一个形参
def foo1(fn):
    print('foo装饰器函数')
    #fn就代表了被装饰的函数：test
    def noname(*args):
        print('---noname函数---')
        fn(*args)
    return noname

#被装饰的函数
#（1）test函数会被作为参数传给foo()装饰器函数
#（2）test函数就被替换成foo装饰器函数的返回值(noname)
@foo1
def test(a, b):
    print('bar函数')
    print('参数a：', a)
    print('参数b：', b)

#表面上是第哦啊用test函数，实际上是调用foo装饰器函数的返回值(noname)
test(2, 4)

print('-' * 50)
#——————————————————————————————————————————————————————————————————

#foo函数，该函数将打算作为函数装饰器使用
#作为函数装饰器使用的函数，它必须定义一个形参
def foo2(fn):
    print('foo装饰器函数')
    #fn就代表了被装饰的函数：test
    def noname(*args):
        print('---模拟在目标函数之前植入的Advice---')
        fn(*args)#目标函数依然在次出调用
        print('---模拟在目标函数之后植入的Advice---')
    return noname

#被装饰的函数
#（1）test函数会被作为参数传给foo()装饰器函数
#（2）test函数就被替换成foo装饰器函数的返回值(noname)
@foo2
def test2(a, b):
    print('bar函数')
    print('参数a：', a)
    print('参数b：', b)

#表面上是第哦啊用test函数，实际上是调用foo装饰器函数的返回值(noname)
test2(2, 4)