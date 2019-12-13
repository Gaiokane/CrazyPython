#book参数支持收集，它可接受多个参数值
def test(num, *books):
    print('num:', num)
    print('books:', books)

#将多个值自动封装成元组
test(5, 'qqq', 'www', 'eee', 'rrr')

print('-' * 50)

def info(*names, msg):
    for name in names:
        print('%s, %s' % (name, msg))

#如果你要为参数收集之后的参数传入参数值，需要用关键字参数
#否则所有参数都会被参数收集成元组
info('qk', 'th', msg='hello')

#每个函数只能有一个参数支持普通的参数收集
#如果python支持在一个函数定义多个支持参数收集的参数，那么python将搞不清楚谁来收集参数值
#def foo(*a, *b, *c):
#    pass

print('-' * 50)

def test1(num, *books, **scores):
    print('num:', num)
    print('books:', books)
    print('scores:', scores)

test1(20, 'qqq', 'www', 'eee', 语文=99, 数学=100)

print('-' * 50)

def info1(*names, msg, **scores):
    for name in names:
        print('%s, %s' % (name, msg))
    print(scores)

#程序知道msg参数将是传给msg的，因此socres不会收集它
#dict的参数收集，它只收集不能明确传入的关键字参数
info1('qk', 'th', msg='hello', 语文=99, 数学=100)

print('-' * 50)

def test2(a, b):
    print(a)
    print(b)

vals = (20, 40)
#调用函数时，python不会对元组自动解包
#默认情况下，元组是一个整体
#test(vals)
#*对元组进行解包（逆向参数收集）
test2(*vals)

print('-' * 50)

msgs = ['qk', 'qkk']
#调用函数时，python不会对元组自动解包
#默认情况下，元组是一个整体
#test(vals)
#*对元组进行解包（逆向参数收集）
test2(*msgs)

print('-' * 50)

vals1 = {'a' : 89, 'b' : 93}

#用字典的逆向收集，以关键字参数的形式为参数传入参数值
#**是将字典解析成关键字参数
test2(**vals1)