class Employee:
    def work(self):
        print('8小时工作')

class Manager(Employee):
    def work(self):
        print('996')

    def relax(self):
        print('休息中')
        #默认情况下，直接调用work方法，总是调用子类重写之后的方法
        #self.work()
        #如果次出希望调用父类的方法，可通过未绑定方法来调用
        #类名调用方法：未绑定方法，因此需要显式传入第一个参数
        Employee.work(self)

mg = Manager()
mg.relax()

print('-' * 50)

class EmployeeSalary1:
    def __init__(self, salary):
        self.salary = salary * 1.8

class ManagerSalary1(EmployeeSalary1):
    def __init__(self, salary, title):
        #当子类的初始化操作与父类初始化操作相同时
        #程序不应该直接复制父类初始化代码——这样不利于后期的项目升级

        #因此，子类构造器应该直接调用父类的构造方法
        #self.salary = salary * 2.1

        #方式一：使用来绑定方法调用父类构造方法：需要显式传入self参数
        EmployeeSalary1.__init__(self, salary)
        self.title = title

mg1 = ManagerSalary1(6800, '项目经理')
print(mg1.salary)
print(mg1.title)

print('-' * 50)

class EmployeeSalary2:
    def __init__(self, salary):
        self.salary = salary * 2.3

class ManagerSalary2(EmployeeSalary2):
    def __init__(self, salary, title):
        #当子类的初始化操作与父类初始化操作相同时
        #程序不应该直接复制父类初始化代码——这样不利于后期的项目升级

        #因此，子类构造器应该直接调用父类的构造方法
        #self.salary = salary * 2.1

        #方式二：用super()函数来调用父类的构造器方法：无需传入self参数
        super().__init__(salary)
        self.title = title

mg2 = ManagerSalary2(6800, '项目经理')
print(mg2.salary)
print(mg2.title)