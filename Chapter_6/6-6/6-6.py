with open('6-5/6-5_1.py', 'rb', True) as f:
    #r模式打开，文件指针位于开始处
    print(f.tell())#0

    #whence默认为0，从开始处开始计算移动
    f.seek(3)
    print(f.tell())#3

    #whence默认为0，从开始处开始计算移动
    f.seek(27)
    print(f.tell())#27

    #whence默认为1，从当前处(27)开始计算移动
    f.seek(27, 1)
    print(f.tell())#54

    #whence默认为1，从当前处(54)开始计算移动
    f.seek(3, 1)
    print(f.tell())#57

    import os
    #getsize可获取文件大小
    print(os.path.getsize('6-5/6-5_1.py'))
    #whence为2，从结尾处开始计算移动
    #offset为0、whence为2，将指针移动到文件的结尾处
    f.seek(0, 2)
    print(f.tell())

    #移动到文件结尾处前10个字节
    f.seek(-10, 2)
    print(f.tell())

    print('-' * 50)

#二进制模式打开，文件输出，一定要用w或a模式
with open('6-6/info1.txt', 'wb', True) as f:
    #输出字节串
    f.write('我是qk'.encode('UTF-8'))

#二进制模式打开，文件输出，一定要用w或a模式
with open('6-6/info2.txt', 'w', True) as f:
    #输出字节串
    f.write('我是qk')

import os
#二进制模式打开，文件输出，一定要用w或a模式
with open('6-6/info3.txt', 'wb', True) as f:
    f.writelines((('你' + os.linesep).encode('GBK'),
    ('的' + os.linesep).encode('GBK'),
    ('名字' + os.linesep).encode('UTF-8')))