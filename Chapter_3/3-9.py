SIZE = 7
array = [[0] * SIZE] #[[0, 0, 0, 0, 0, 0]]
#得到一个SIZE* SIZE的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]

#控制方向
#0代表向下，1代表向右，2代表向左，3代表向上
orient = 0

#j控制行，k控制列
j, k = 0, 0
#控制程序将1~SIZE*SIZE的数填入二维数组
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    #1号转弯线
    if j + k == SIZE - 1:
        #行大于列，位于下半
        if j > k:
            orient = 1
        #位于上半
        else:
            orient = 2
    #位于2号转弯线，方向改为向上（3）
    elif j == k and j >= SIZE / 2:
        orient = 3
    #位于3号转弯线
    elif j + 1 ==k and k <= SIZE / 2:
        orient = 0
    
    if orient == 0: #0代表向下
        j += 1
    elif orient ==1: #1代表向右
        k += 1
    elif orient == 2: #2代表向左
        k -= 1
    elif orient == 3: #3代表向上
        j -= 1

#array是一个二维列表（列表嵌套列表），array的元素又是列表
for ele in array:
    for e in ele:
        print('%02d' % e, end = ' ')
    print('')