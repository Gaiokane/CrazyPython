class Fruit:
    def taste(self):
        print('水果好吃')

#Apple继承了Fruit
class Apple(Fruit):
    pass

a = Apple()
#继承的好处：子类可以直接复用父类的方法
a.taste()

print('-' * 50)

class Product:
    def produce(self):
        print('Product类中的produce方法')
    def info(self):
        print('Product类中的info方法')

class Foo:
    def produce(self):
        print('Foo类中的produce方法')

#子类继承父类，子类会获得父类的方法
#排在前面的父类中的方法，将会优先被继承
class Item(Foo, Product):
    pass

im = Item()
im.produce()

print('-' * 50)

class Bird:
    def fly(self):
        print('鸟会飞')

class Ostrich(Bird):
#父类的方法并不适合子类，子类可以定义与父类同名的方法，这就是方法重写
    def fly(self):
        print('鸵鸟不会飞')

os = Ostrich()
os.fly()