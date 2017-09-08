#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态

class Animal(object):

    def __init__(self):
        self.x = 9

    def run(self):
        print('Animal is runing...')



class Dog(Animal):

    def run(self):
        print('Dog is runing...')

class Cat(Animal):

    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()

cat = Cat()
cat.eat()


def run_twice(animal):
    animal.run()

run_twice(Dog())
run_twice(Cat())

# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。


# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。


#判断对象类型
print(type(dog))

a = Animal()
b = Dog()
c = Cat()
print(isinstance(a, Dog))
print(isinstance(c, Cat))

# 获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(c))
print(c.__str__())

print(hasattr(a, 'x'))  # 有属性'x'吗？
setattr(b, 'y', 5)  # 设置一个属性'y'
print(hasattr(b, 'y'))  # 有属性'y'吗？
print(getattr(b, 'y'))  # 有属性'y'吗？
print(b.y)

print(getattr(b, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

fn = getattr(b, 'run')  # 获得对象的方法，并赋值
b.run()
fn()