'''
1  2  3  4
5  6  7  8
9 10 11 12

转置：行变列，列变行

1  5  9
2  6 10
3  7 11
4  8 12
'''

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def printmatrix(m):
    #是列表嵌套列表，因此ele也是列表
    for ele in m:
        #打印一行
        for e in ele:
            print('%2d' % e, end = ' ')
        print('')

def transformatrix1(m):
    #m[0]有几个元素，说明原矩阵有多少列
    #列转成了行
    rt = [[] for i in m[0]]
    for ele in m:
        for i in range(len(ele)):
            #rt[i]代表新矩阵的第i行
            #ele[i]代表原矩阵当前行的第i列
            rt[i].append(ele[i])
    return rt

def transformatrix2(m):
    #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    #zip([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]) ->(1, 5, 9), ...
    #逆向参数收集，将矩阵中多个列表转换成多个参数，传给zip
    return list(zip(*m))

def transformatrix3(m):
    #使用numpy的transpose()函数
    import numpy
    return numpy.transpose(m).tolist()

printmatrix(matrix)

print('-' * 50)

printmatrix(transformatrix1(matrix))

print('-' * 50)

printmatrix(transformatrix2(matrix))

print('-' * 50)

printmatrix(transformatrix3(matrix))