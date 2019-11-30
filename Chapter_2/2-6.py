scores = {'语文': 67, '数学': 77, '英语': 87}
print(scores)
#用一个字典（字典、序列、关键字参数）来更新原有的字典
#对于已有的key，是更新value；对于不存在的key，就是添加key-value对
scores.update({'语文': 7, '生物':91})
print(scores)

#使用序列作为参数，此时序列的每个元素都只能有2个元素：第一个是key，第二个是value
scores.update([('语文', 77), ('物理', 777)])
print(scores)

#使用关键字参数，不支持用表达式
scores.update(语文=1, 化学=2)
print(scores)

print('————————————————————————————————————————————————')

#遍历key
for key in scores.keys():
    print(key)
#遍历value
for value in scores.values():
    print(value)
#遍历key,value（序列解包）
for key, value in scores.items():
    print(key, value)
print('————————————————————————————————————————————————')
print(scores)
#setdefault用于获取指定key对应的value
print(scores.setdefault('语文', 100))
#setdefault如果获取的key不存在时，该方法会为该key设置value
print(scores.setdefault('qqq', 7777777))
print(scores)
print('————————————————————————————————————————————————')
#fromkeys方法可将序列转换成字典（使用固定的值作为value）
sc = dict.fromkeys(['语文', '数学', '英语'])
print(sc)

sc2 = dict.fromkeys(['语文', '数学', '英语'], 77)
print(sc2)
print('————————————————————————————————————————————————')
s1 = '图书名为：%s, 价格为： %10.2f'
#用元组来格式化字符串，所以它根据位置来填充“占位符”
print(s1 % ('疯狂Python讲义', 128)) 

s2 = '图书名为：%(name)s, 价格为： %(price)10.2f'
#用dict来格式化字符串，所以它根据key来填充“占位符”
print(s2 % {'price': 128, 'name': '疯狂Python讲义'})