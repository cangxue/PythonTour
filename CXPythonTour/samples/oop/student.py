#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):


    def __init__(self, name, score):
        self.name = name
        self.score = score

        # 实例的变量名如果以__开头，就变成了一个私有变量（private），
        # 只有内部可以访问，外部不能访问，所以
        self.__date = '2017 - 9 - 10'
        self.__age = 18

    # 外部代码要获取date
    def get_date(self):
        return self.__date

    def get_age(self):
        return self.__age

    # 允许外部代码修改date
    def set_date(self, date):
        self.__date = date

    def set_age(self, age):
        if 0 <= age <= 200:
            self.__age = age
        else:
            return ValueError('bad age')

    def print_score(self):

        print('%s: %s' % (self.name, self.score))

    def print_date(self):
        print('%s' % self.__date)



    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
bart.name = 'cangxue'
lisa = Student('Lise Simpos', 87)

bart.print_score()
lisa.print_score()
print(bart.get_grade())


bart.age = 8
print(bart.age)
bart.print_date()

print(bart.get_date())
bart.set_date('2017 - 9 - 11')
print(bart.get_date())

bart.set_age(299)
print(bart.get_age())
