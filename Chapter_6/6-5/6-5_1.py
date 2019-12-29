import sys

#sys.stdin代表系统的标准输入（键盘），它是一个类文件的对象
#遍历文件（把sys.stdin当成文件来看）的语法
#for line in sys.stdin:
#    print(line)

#默认情况下，sys.stdin是从键盘读取
#如果使用管道输入之后，sys.stdin将改为从前一个程序的输出来读取

#程序要使用python将javac命令的输出中有关'module'的行，都打印出来
for line in sys.stdin:
    #如果读到这一行包含了'module'，输出该行内容
    if 'module' in line:
        print(line)