#列表推导式的循环控制的不是循环，而是前面的表达式
#循环几次，前面的表达式执行多少次，表达式的多次执行结果将作为列表的元素
#对于列表推导式而言，for循环执行几次，那么列表就有几个元素
r = ['表达式' for i in range(10)]
print(r)

r = [i * 2 for i in range(10)]
print(r)

r = [i * i for i in range(20)]
print(r)

#计算1、100的总和，sum对整个列表元素求和
print(sum([i for i in range(1, 101)]))

print('————————————————————————————————————————————————')

for i in range(10):
    print(i)
    #break可提前结束循环
    if i > 5:
        break
#跳出循环后，else不会执行
else:
    print('循环结束')

print('————————————————————————————————————————————————')

for i in range(10):
    print(i)
    #continue忽略本次循环剩下的语句
    if i > 5:
        continue
    print('当前是第%d次循环' % i)