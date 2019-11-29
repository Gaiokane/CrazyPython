my_list = ['q', 'w']

my_list.append('e')
print(my_list)
#为列表append元组，元组将被当成整体
my_list.append(tuple(range(3, 6)))
print(my_list)
#extend方法用于将序列中的元素添加进来
my_list.extend(range(20, 25))
print(my_list)
#字符串也是序列
my_list.extend("qkk")
print(my_list)
#将r插入到第4个元素
my_list.insert(3,'r')
print(my_list)

print('——————————————————————————————————————')

#删除第三个元素
del my_list[2]
print(my_list)
#删除第五个到第7个
del my_list[4: 7]
print(my_list)
#指定步长删除
del my_list[4: 9 : 2]
print(my_list)

#对单个元素赋值
my_list[-3] = 'e'
print(my_list)
#被替换部分只有2个元素，替换成4个元素，实际是增加了元素
my_list[2: 4] = ['e', 'r', 't', 'y']
print(my_list)
#被替换部分只有2个元素，替换成1个元素，实际是删除了元素
my_list[6: 8] = ['u']
print(my_list)
#当列表中一段赋值时，程序会自动把字符串当成列表处理
my_list[6: 7] = 'uiop'
print(my_list)

print('——————————————————————————————————————')

print(my_list.index('r'))#获取元素的位置
my_list.reverse()#反转
print(my_list)
my_list.sort()#排序
print(my_list)