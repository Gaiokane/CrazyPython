#创建列表用方括号
#列表所包含的元素是可以改变的
my_list = [1,2,'qk',7.7]
print(my_list)

#创建元组用圆括号
#元组一旦创建，它所包含的元素是不能改变的
my_tuple = (7.7,2,'Gaiokane')
print(my_tuple)

#如果创建的元组只有一个元素，一定要在元素的后面添加逗号
single_tuplr_err = ('qqq')
print(single_tuplr_err)
single_tuplr = ('qqq',)
print(single_tuplr)

#用list函数创建列表
my_list1 = list(range(2, 10))
print(my_list1)

#用tuple函数创建列表
my_tuple1 = tuple(range(4, 8))
print(my_tuple1)

#将元组转成list
list1 = list(my_tuple1)
print(list1)

#将list转成元组
tuple1 = tuple(my_list1)
print(tuple1)