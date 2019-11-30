NUM = 10
import random

#方法一
#创建空列表
result = []
#循环10次，生成10个随机数
for i in range(NUM):
    #生成65-90（不包括）的随机数
    n = random.randint(65, 90)
    #随机数转成字符，并添加到列表
    result.append(chr(n))
print(result)
print('————————————————————————————————————————————————————————')
#方法二
#列表推导式
#chr(random.randint(65, 90)) 表达式负责生成随机的大写字符
result = [chr(random.randint(65, 90)) for i in range( NUM)]
print(result)
print('————————————————————————————————————————————————————————')
#方法三
#使用numpy模块
import numpy
#numpy.random.randint()函数可生成一个随机数的矩阵，可生成多行、多列的随机数

#numpy.random.randint(65, 90, [NUM, 1])可生成1列、NUM行个随机数（相当于一个包含NUM个随机数的列表）
result = [chr(i) for i in numpy.random.randint(65, 90, [NUM, 1])]
print(result)