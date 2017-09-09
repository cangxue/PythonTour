#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from types import MethodType

class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score  # 给class绑定方法：

s2 = Student()
s2.set_score(100)
print(s2.score)

# ----------------------- 分割线 ------------------------------

# 使用__slots__

class Student2(object):

    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student2):
    pass

s = Student2() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)