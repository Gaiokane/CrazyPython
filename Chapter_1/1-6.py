#比较运算符
a=int(input('请输入a：'))
b=int(input('请输入b：'))
print(a>=b)

s1='123'
s2=str(123)
print(s1 is s2)#不是同一个对象 精确判断
print(s1==s2)#==判断值是否相等

#逻辑运算符
print(3**3>30 and 3**3>20)#与
print(3**3>30 or 3**3>20)#或
print(not 1>3)#非


#三目运算符
age = int(input('请输入年龄：'))
print('年龄大于20') if age > 20 else print('年龄小于或等于20')
print('年龄大于20') if age > 20 else print('年龄等于20') if age == 20 else print('年龄小于20')
s=print('年龄大于20'),'qqq' if age > 20 else print('年龄小于或等于20')
print(s)#，返回元组，(None, 'qqq') 返回none是因为print语句没有返回值
s=print('年龄大于20');'qqq' if age > 20 else print('年龄小于或等于20')
print(s)#；返回元组中第一个值

#in 判断序列是否包含某个成员
s='gaiokane'
print('x' in s)
print('a' in s)