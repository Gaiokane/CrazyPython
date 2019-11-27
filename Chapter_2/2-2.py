my_tuple = tuple(range(3, 10))
print(my_tuple)

#len()函数可用于访问列表的长度
print(len(my_tuple))

print(my_tuple[2])#第三个元素
print(my_tuple[-2])#倒数第二个元素

my_list = ['q','w','e','r','t','y']
print(my_list[3])
print(my_list[-3])

#当用索引访问元素时，索引必须在 -len 至 len-1 之间，否则程序会报错：list index out of range
#print(my_list[6])
print(my_list[-6])

my_tuple1 = ('q','w','e','r','t','y','u','i','o','p')

#获取子序列（中间一段）
print(my_tuple1[2: 5])
print(my_tuple1[-5: -2])
print(my_tuple1[3: -1])

#指定step
print(my_tuple1[2: -1: 2])
print(my_tuple1[2: -1: 3])

list1 = ['q','w']
list2 = list(range(4))

#加法就是把两个列表的元素拼接在一起
print(list1 + list2)

tuple1 = ('q', 'w')
tuple2 = tuple(range(4))

#加法就是把两个元组的元素拼接在一起
print(tuple1 + tuple2)

#列表和元组不能相加，若要相加要先进行转换
print(list1+list(tuple2))
print(tuple(list1)+tuple2)

#序列只能与整数相乘，就是把元素重复N次
print(list2 * 3)
print(tuple2 * 5)

#字符串也属于序列，银子字符串也支持与int相乘
s = 'qkk'
print(s * 5)

#in判断元素是否存在序列/元组中
list3 = list(range(7))
print(3 in list3)
print(7 in list3)