for i in range(10):
    #i的值会被for-in接管，i的值会自动依次等于range中每个元素的值
    print(i)

print('————————————————————————————————————————————')

my_data = {'q': 1, 'w': 2, 'e': 3, 'r': 4}
#my_data的values()返回值本身就是一个可迭代对象
#values()返回字典的所有value
for v in my_data.values():
    print(v)
print('————————————————————————————————————————————')
#my_data的keys()返回值本身就是一个可迭代对象
#keys()返回字典的所有keys
for v in my_data.keys():
    print(v)

print('————————————————————————————————————————————')

#python支持在循环中添加else块，但这个else块与直接放在循环后面效果大致相同
for c in 'Gaiokane':
    print(c)
#当循环结束时，程序执行else块
else:
    print('循环结束')

print('————————————————————————————————————————————')

'''
对于外层循环而言，内存循环酒相当于一条语句
当内层循环执行N次，外层循环执行M次，内层循环的循环体一共会执行NxM次
'''

for i in range(10):
    j=0
    while j < 20:
        print("i:%d, j:%d" % (i, j))
        j += 1