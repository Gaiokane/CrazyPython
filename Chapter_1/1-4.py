a = '\nq\rw\re'
print(a)

s1 = '我是%s，%s'
print(s1 % ('Gaiokane','hhh'))

#下标访问
s2 = 'gaiOkane'
print(s2[2])
print(s2[2:6])#开始结束 包含开始不包含结束
print(s2[2:6:2])#开始结束间隔 包含开始不包含结束
print('q' in s2)#判断是否包含 不包含false
print('k' in s2)#判断是否包含 包含true
print(len(s2))#获取长度
print(max(s2))#获取最大值
print(min(s2))#获取最小值
print(s2.title())#单词首字母大写
print(s2.lower())#全小写
print(s2.upper())#全大写
print(dir(str))#查看类的方法
print(help(str.islower))#查看用法
print(' hhh '.strip() + '1')#删除字符串前后的空格
print(' hhh '.lstrip() + '1')#删除字符串前的空格
print(' hhh '.rstrip())#删除字符串后的空格
print(help(str.startswith))
print(s2.startswith('G'))#是否以G开头
print(s2.endswith('e'))#是否以e结尾
print(s2.find('ai'))#查找是否在字符串中出现，有1 没有-1
print(s2.index('Ok'))#查找指定字符在字符串中的位置，没有 报错
print(s2.replace('O','hhh'))#替换
print(s2.split('i'))#分割
print(s2.split('i')[1])#分割 并显示第二块
print('='.join(s2.split('i')))#连接
print('7'.join(s2))