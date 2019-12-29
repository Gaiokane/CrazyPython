class User:
    def __init__(self, age):
        #要求age必须在10到30岁之间
        if age > 30 or age < 10:
            raise#RuntimeError异常
        self.__age = age
    
    def setage(self, age):
        #要求age必须在10到30岁之间
        if age > 30 or age < 10:
            #raise#RuntimeError异常
            #raise ValueError#引发指定类的默认异常对象
            raise ValueError(age, '年龄必须在10~30之间')#引发异常对象
        self.__age = age
    def getage(self):
        return self.__age
    age = property(fget=getage, fset=setage)

user = User(25)
print(user.age)
try:
    user.age = 45
except ValueError as e:
    print(e.args)