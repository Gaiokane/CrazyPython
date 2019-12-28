try:
    f1 = open("Chapter_6/6-4/登高.txt", 'r', True)
    # 采用循环依次读取多行
    while True:
        line = f1.readline()
        # 如果没有读取一行，说明文件已经读完了
        if not line:
            break  # 跳出循环
        print(line, end='')
# 如果不需要处理具体的异常对象，只要except就够了
except:
    # 这种方式就无法访问异常对象
    print('出现了异常')
finally:
    if 'f1' in globals():
        f1.close()


print('\n' + '-' * 50)


try:
    f2 = open("Chapter_6/6-4/登高.txt", 'r', True)
    # 直接读取所有行，返回所有行组成的列表
    lines = f2.readlines()
    print(lines)
# 如果不需要处理具体的异常对象，只要except就够了
except:
    # 这种方式就无法访问异常对象
    print('出现了异常')
finally:
    if 'f2' in globals():
        f2.close()


print('\n' + '-' * 50)


try:
    f3 = open("Chapter_6/6-4/登高.txt", 'r', True)
    
    #文件对象本身就是可迭代的，因此直接用for-in循环迭代即可
    for line in f3:
        print(line, end='')
# 如果不需要处理具体的异常对象，只要except就够了
except:
    # 这种方式就无法访问异常对象
    print('出现了异常')
finally:
    if 'f3' in globals():
        f3.close()


print('\n' + '-' * 50)


import linecache
try:
    #通过linecache随机读取指定行时，甚至不需要处理打开文件
    #linecache主要读取python源文件，因此它要求文件内容是UTF-8字符集
    #print(linecache.getline('Chapter_6/6-4/登高.txt', 2))
    
    #任何模块，访问它的__file__属性，该属性将返回该模块的源文件的完整路径
    print(linecache.getline(linecache.__file__, 3))

    print('-' * 50)

    #读取linecache模块的所有文件内容
    for line in linecache.getlines(linecache.__file__):
        print(line, end='')
# 如果不需要处理具体的异常对象，只要except就够了
except:
    # 这种方式就无法访问异常对象
    print('出现了异常')