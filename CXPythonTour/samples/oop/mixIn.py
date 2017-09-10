#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承

class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Runing...')

class Mammal(Animal):
    pass


class Dog(Mammal, Runnable):
    pass

d = Dog()
d.run()