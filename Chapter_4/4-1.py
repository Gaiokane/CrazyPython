def first():
    print('这是第一个函数')
    for i in range(5):
        print('i的值：', i)

#调用函数
first()
first()

print('—' * 50)

def hello(name):
    print('你好，', name)

hello('Gaiokane')

print('—' * 50)

def max(a, b):
    if a > b:
        print('最大值为：', a)
    else:
        print('最大值为：', b)

max(1,2)

print('—' * 50)

def getmax(a, b):
    '''
    getmax(a, b)
    传入a和b返回最大值
    '''
    result = a if a > b else b
    return result

print('最大值为：',getmax(3,7))
print(help(getmax))