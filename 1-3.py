#字符串入门

#使用不同引号
s1 = "it's Gaiokane"
print(s1)

#使用转义
s2 = 'it\'s Gaiokane'
print(s2)

#--------------------

int1 = 7
str1 = 'qk'
str2 = 'QK'

#字符串相加 +
str3 = str1 + str2
print(str3)

str3 = str(int1) + str1
print(str3)

str3 = repr(int1) + str1
print(str3)

print(repr(str2))

str4 = repr(str2)
print(str4)

#获取输入
inp = input("请输入：")
print("输入的是：" + inp)

#长字符串
longstr = '''qqq
kkk
qkk
'''
print(longstr)
longstr = '''qqq\nkkk\nqkk\n'''
print(longstr)

#原始字符串 直接输出
rs = r'qqq\nkkk'
print(rs,type(rs))
#'还是要转义
rs = r'qqq\'kkk'
print(rs)

#字节串
bs1 = b'qqq'
print(bs1,type(bs1))

bs2 = '字节串'.encode()
print(bs2,type(bs2))

bs3 = bytes('字节串','utf-8')
print(bs3,type(bs3))

bs4 = b'\xe5\xad\x97\xe8\x8a\x82\xe4\xb8\xb2'
print(bs4.decode('utf-8'))