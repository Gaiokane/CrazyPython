try:
    #将所有可能出现异常的代码，放在try块中执行
    
    #rb代表以二进制形式来读取文件内容
    #rb模式读取文件，可用于处理任意文件内容：比如图片、音乐、视频等格式
    f1 = open("Chapter_6/6-3/登高.txt", 'rb', True)
    #由于目标文件以GBK字符集保存，在这种字符集下，每个字符占2个字节

    #二进制模式读取时，read方法返回值是bytes（字符串）
    data = f1.read(4)

    print(str(data, 'GBK'))

#捕捉所有的OSError异常，异常对象叫e
except OSError as e:
    print(e)
    print(e.args)#异常参数
    print(e.errno)#异常编号
    print(e.strerror)#异常描述信息

#finally块代表无论异常，还是正常，总会执行的代码块
#由于它总会执行，因此finally块通常用于关闭资源
finally:
    #当f变量存在时，关闭f文件流
    if 'f1' in globals():
        print('关闭文件')
        #关闭文件流
        f1.close()
        print('-' * 50)





try:
    #按字符读，建议指定字符集（根据目标文件的字符集来设置）
    f2 = open("Chapter_6/6-3/登高.txt", 'r', True, 'GBK')

    #按字符读，read方法的返回值就是字符串
    data = f2.read()

    print(data)

#捕捉所有的OSError异常，异常对象叫e
except OSError as e:
    print(e)
    print(e.args)#异常参数
    print(e.errno)#异常编号
    print(e.strerror)#异常描述信息

#finally块代表无论异常，还是正常，总会执行的代码块
#由于它总会执行，因此finally块通常用于关闭资源
finally:
    #当f变量存在时，关闭f文件流
    if 'f2' in globals():
        print('关闭文件')
        #关闭文件流
        f2.close()
        print('-' * 50)