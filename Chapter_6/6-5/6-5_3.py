class Resource:
    def __init__(self, tag):
        print('--构造方法--')
        self.tag = tag
    #进入with语句时会执行该方法
    def __enter__(self):
        print('该资源的tag：', self.tag)
        #此处的返回值就是as子句中变量的值
        return 'Gaiokane'
    
    '''
    这三个参数都代表了异常
    ex_type：异常类型
    ex_value：异常value，就是你创建异常时传入所有参数值
    ex_traceback：异常的traceback
    '''
    def __exit__(self,ex_type, ex_value, ex_traceback):
        #ex_traceback存在，说明因为异常退出
        if ex_traceback:
            print('因为异常关闭资源')
        else:
            print('程序正常结束，关闭资源')

#(1)执行with子句后的表达式（Resource('qk')）
#(2)执行__enter__方法，并将该方法的返回值赋值给as子句中的变量
#(3)__exit__方法，在with语句块执行完成或遇到异常时自动执行
with Resource('qk') as fk:
    print('fk为：', fk)
    print('before')
    #raise Exception(20, '自定义异常')
    print('after')