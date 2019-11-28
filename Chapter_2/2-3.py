my_list = list(range(7))
print(my_list)
print(len(my_list))
print(min(my_list))
print(max(my_list))

print('—————————————————————')

my_tuple = tuple(range(7))
print(my_tuple)
print(len(my_tuple))
print(min(my_tuple))
print(max(my_tuple))

print('—————————————————————')

list1 = ['aa','ab']
print(max(list1))#字符串也能比较大小，逐字符对应编码

qk = 7, 'qkk'#封包
print(qk)
print(type(qk))

a, b = qk#解包
print(a)
print(b)

q, w, e = range(3)#所有序列（包括range）都支持自动解包
print(q, w, e)

tuple1 = ['111','222','333','444']
fir, *sec = tuple1#如果只想解包某一个值，剩下的值可用一个带*的变量（列表）来接收
print(fir)
print(sec)


fir, *sec, last = tuple1#如果只想解包某几个值，剩下的值可用一个带*的变量（列表）来接收
print(fir)
print(sec)
print(last)

a, b, *c = 'qwertyuiop'#字符串也是序列，也支持解包
print(a)
print(b)
print(c)

#先将右边多个值封包成元组
#元组又被解包依次对3个变量赋值
a, b, c = 30, 'py', 7.7
print(a)
print(b)
print(c)