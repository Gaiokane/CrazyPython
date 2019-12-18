#User类
class User:
    '''
    User类
    '''
    print('User类')

#Item类
class Item:
    '''
    Item类
    '''
    print('Item类')

    #类空间中定义的变量，属于类变量
    itemtype = '分类1'
    itemname = 'qqq'

print('分类：', Item.itemtype)
print('名字：', Item.itemname)
#python是动态语言，你随时可以为类增加类变量
#只要对类引用的变量赋值，就是增加新的类变量
Item.foo = '测试类变量'
print(Item.foo)

#随时也可以删除类变量
del Item.itemtype
#所以下面程序报错：itemtype类变量已经被删除
#print('分类：', Item.itemtype)

class Book:
    print('Book')
    booktype = '图书类别'

    #定义方法与定义函数几乎一样
    #实例方法，第一个参数推荐使用self（并不强制），这样有更好的可读性
    def desc(self):
        self.name = '书名'
        self.price = 77
        print('图书是%s, 价格是%d' % (self.name, self.price))

    def gai(self):
        print('Gaiokane')