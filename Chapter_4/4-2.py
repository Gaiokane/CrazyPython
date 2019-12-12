import random

def GetThreeRandomChar():
    #生成3个随机的大写字符
    c1 = chr(random.randint(65, 90))
    c2 = chr(random.randint(65, 90))
    c3 = chr(random.randint(65, 90))

    #以元组形式返回
    #return (c1, c2, c3)#同下
    return c1, c2, c3

result = GetThreeRandomChar()#result就是一个元组
print(result)
print(GetThreeRandomChar())#元组

#多返回值函数，既可用多个变量来接收返回值，也可用单个变量来接收返回值
#多个变量，执行自动解包
c1, c2, c3 = GetThreeRandomChar()
print(c1)
print(c2)
print(c3)

c1, *c2 = GetThreeRandomChar()
print(c1, c2)

*c1, c2 = GetThreeRandomChar()
print(c1, c2)

print('-' * 50)

#计算n的阶乘
def frac(n):
    if n < 1:
        print('n不能小于1')
        return
    elif n == 1:
        return 1
    else:
        #n的阶乘总是等于上一个阶乘 * n
        #函数调用自身
        return frac(n - 1) * n
#该递归函数的结束点是n==1，因此一定要向n==1去递归

print(frac(5))
print(frac(6))