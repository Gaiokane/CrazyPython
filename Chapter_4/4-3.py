def info(name, age, height):
    print('name:', name)
    print('age:', age)
    print('height:', height)

#位置参数
info('qk', 23, 174)

print('-' * 50)

#关键字参数（命名参数），不需要按顺序
#又是：1.不需要按顺序，2.可读性更高
info(age=24, name='Gaiokane', height=175)

print('-' * 50)

#混合使用
#关键字参数必须位于位置参数的后面
info('qqq', height=177, age=7)

print('-' * 50)

#定义带默认值的参数
def defaultinfo(age, name='qaq'):
    print('name:', name)
    print('age:', age)

defaultinfo(23)
defaultinfo(34, 'QAQ')

print('-' * 50)

def sayhi(name='qk', message='你好'):
    print('name:', name)
    print('message:', message)

sayhi()
sayhi('QK')
sayhi(message='hello')