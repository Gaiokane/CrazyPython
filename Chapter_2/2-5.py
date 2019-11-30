#三种方式创建字典
#字典（dict）是可变的，列表也是可变的
#列表的元素可增、删、改，字典中的key-value对也可增、删、改
#字典中的数据就是key: value成对出现
scores = {'语文': 67, '数学': 77, '英语': 87}
print(scores)
#要求每个元素只能有2个元素，其中第一个元素是key，第二个元素是value
my_dict = dict([('语文', 67), ('数学', 77), ('英语', 87)])
print(my_dict)
#用关键字参数来创建dict，此时不允许使用表达式
my_dict2 = dict(语文 = 67, 数学 = 77, 英语 = 87)
print(my_dict2)

#通过key访问value
print(scores['语文'])
#对不存在的key赋值，就是添加key-value对
scores['qq'] = 7
print(scores)
#对已有的key赋值，就是替换key-value对
scores['数学'] = 777
print(scores)
#删除key-value对
del scores['qq']
print(scores)

print('———————————————————————————————————————')
#使用in、not in可判断dict是否包含指定key
#判断是否包含，只要判断key
print('qq' in scores)
print('存在') if '语文' in scores else print('不存在')

#list从0开始，dict下标可以任意