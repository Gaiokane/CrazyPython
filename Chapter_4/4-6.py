def foo():
    print('foo函数')
    #局部函数：在其他函数内定义的函数
    def bar():
        for i in range(5):
            print('bar函数', i)
    #bar表示函数本身（函数也相当于一个值，是function类型的值）
    #bar()表示调用（执行）函数
    return bar

#局部函数只在它所在封闭函数内有效
#bar()

#foo()函数的返回值是bar函数，因此此处就是用r变量来保存bar函数
r = foo()
#r()
print(r)
#此时e引用bar函数本身，因此r的类型是function
print(type(r))
print('-' * 50)
#由于r是函数，因此程序可以调用它
r()

print('-' * 50)

#foo()调用之后返回bar函数，bar函数也可调用
foo()()

print('-' * 50)

def test():
    name = 'qk'
    def info():
        print('info函数')
        #声明后面的name变量不是声明新的局部变量，而是引用所在封闭函数的局部变量
        nonlocal name
        print('name:', name)
        #默认情况下，下面代码是为info局部函数再次定义name局部变量
        #此时name局部变量就会hide test函数内的name局部变量
        #如果前面用了nonlocal name，此时就是对封闭函数的name局部变量赋值
        name = 'qkk'
        print('name:', name)
    info()
    print(name)

test()