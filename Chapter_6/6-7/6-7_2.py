f = None
try:
    #f = open('6-7/abc.txt', 'r', True)
    f = open('6-7/6-7_1.py', 'r', True)
    print(f.read())
except:
    print('捕捉到异常')
finally:
    #程序要判断f不为None才需要close
    if f:
        #在finally块中嵌套了异常处理
        try:
            print('关闭文件')
            f.close()#close本身可能引发异常
        except:
            print('关闭文件时有异常')