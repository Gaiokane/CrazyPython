#w模式准备写文件，清空文件内容
#open("Chapter_6/6-2/mydata.txt",'w')

#w+模式:读写模式，清空文件内容
#open("Chapter_6/6-2/mydata.txt",'w+')

#r+模式:读写模式
#r、r+都要求打开的文件存在，否则程序报错
#open("Chapter_6/6-2/info.txt",'r')

#a模式:追加模式
#a、a+都不要求打开的文件存在，如果文件不存在，自动创建新文件
open("Chapter_6/6-2/info1.txt",'a')
open("Chapter_6/6-2/info2.txt",'a+')

#w模式:写模式
#w、w+都不要求打开的文件存在，如果文件不存在，自动创建新文件
open("Chapter_6/6-2/abc1.txt",'w')
open("Chapter_6/6-2/abc2.txt",'w+')