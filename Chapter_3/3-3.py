i = 0
while i < 10:
    print('i的值%d' % i)
    i += 1

print('——————————————————————————————————————')

my_data = ['q','w','e','r','t','y']
i = 0
while i < len(my_data):
    print(my_data[i])
    i += 1

print('——————————————————————————————————————')

my_data1 = {'q': 1, 'w': 2, 'e': 3, 'r': 4}
i = 0
#将字典所有的key转换成list
keylist = list(my_data1.keys())
#print(keylist)
#通过让下标从0循环到len-1，这样即可遍历列表
while i < len(keylist):
    print(keylist[i], my_data1[keylist[i]])
    i += 1

print('——————————————————————————————————————')

s = 'Gaiokane'
#s（序列）有几个元素，for-in循环就重复几次，循环计数器会自动、依次等于每个元素
for c in s:
    print(c)

print('——————————————————————————————————————')

s = (11,22,33,4,55,66)
for c in s:
    print(c)

print('——————————————————————————————————————')

#用了序列的解包来同时遍历key、value
for key, value in my_data1.items():
    print(key, value)