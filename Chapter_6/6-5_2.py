#使用with语句来关闭资源
try:
    with open('6-5_1.py', 'r', True, 'UTF-8') as f:
        for line in f:
            print(line, end='')
except OSError as e:
    print('有异常', e)