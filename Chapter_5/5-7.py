class User:
    def __init__(self, name='Noname', passwd='pwd'):
        #此处两个实例变量以__开头，因此它会被隐藏
        if isinstance(name, str) and 4 <= len(name) <= 8:
            self.__name = name
        else:
            self.__name = 'Noname'
        if isinstance(passwd, str) and 6 <= len(passwd) <= 12:
            self.__passwd = passwd
        else:
            self.__passwd = 'pwd'

    def getname(self):
        return self.__name
    def setname(self, name):
        '''
        当程序通过setter方法对实例变量赋值时，程序会对所赋的值进行检查
        从而避免传入无效的值，程序可保证对象的完整性
        '''
        if isinstance(name, str) and 4 <= len(name) <= 8:
            self.__name = name
        else:
            print('用户名无效，不是字符串或长度不在4-8位之间')
    name = property(fget=getname, fset=setname)

    def getpasswd(self):
        return self.__passwd
    def setpasswd(self, passwd):
        '''
        当程序通过setter方法对实例变量赋值时，程序会对所赋的值进行检查
        从而避免传入无效的值，程序可保证对象的完整性
        '''
        if isinstance(passwd, str) and 6 <= len(passwd) <= 12:
            self.__passwd = passwd
        else:
            print('密码无效，不是字符串或长度不在6-12位之间')
    passwd = property(fget=getpasswd, fset=setpasswd)

u = User()
#如果没有封装机制，u.name可以被赋值为任意内容
#当使用封装之后，u.name只能设置为4-8位的字符串
u.name = 'qk'
print(u.name)
u.name = 1111111
print(u.name)
u.name = 'Gaiokane'
print(u.name)

print('-' * 50)

class Item:
    def __init__(self):
        #被隐藏的__name变量
        self.__name = 'qkk'

im = Item()
#被隐藏的，下面代码出错
#print(im.__name)
#python会修改__开头的成员名，会将它们的名字增加_类名
print(im._Item__name)