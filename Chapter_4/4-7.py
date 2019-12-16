def fract1(n):
    r = 1
    if n < 1:
        print('n不能小于1')
        return
    else:
        #i从1循环到n
        for i in range(1, n + 1):
            r *= i
        return r

#————————————————————————————————————————————————————————————————————————————#

def fract2(n):
    if n < 1:
        print('n不能小于1')
        return
    #对于递归函数来说，必须保证在某个条件下，函数不再调用自身，递归结束
    elif n == 1:
        return 1
    else:
        #递归：函数里调用自身
        return fract1(n - 1) * n

#————————————————————————————————————————————————————————————————————————————#

import functools
def fn(x, y):
    return x * y
def fract3(n):
    if n < 1:
        print('n不能小于1')
        return
    else:
        #fn(ele1, ele2) -> r
        #fn(r, ele3) -> r
        #fn(r, ele4) -> r
        return functools.reduce(fn, range(1, n + 1))

#————————————————————————————————————————————————————————————————————————————#

def fract4(n):
    if n < 1:
        print('n不能小于1')
        return
    else:
        #fn(ele1, ele2) -> r
        #fn(r, ele3) -> r
        #fn(r, ele4) -> r
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))

#————————————————————————————————————————————————————————————————————————————#

print(fract1(5))
print(fract1(6))
print(fract1(7))

print('-' * 50)

print(fract2(5))
print(fract2(6))
print(fract2(7))

print('-' * 50)

print(fract3(5))
print(fract3(6))
print(fract3(7))

print('-' * 50)

print(fract4(5))
print(fract4(6))
print(fract4(7))

print('-' * 50)