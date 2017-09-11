#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __str__()返回用户看到的字符串
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__  # __repr__()是为调试服务的

    def __getattr__(self, item):  # 动态返回一个属性
        if item == 'score':
            return 99

        if item == 'age':
            return lambda: 25

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    # 只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)

print(Student('Michael'))
s = Student('Michael')
print(s.name)
print(s.score)
print(s.age())
# print(s.date)
s()

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(max))

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    # 如果一个类想被用于for ... in循环，类似list或tuple那样，
    # 就必须实现一个__iter__()方法
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值

        if self.a > 100:  # 退出循环的条件
            raise StopIteration()

        return self.a  # 返回下一个值


    # 要表现得像list那样按照下标取出元素，
    # 需要实现__getitem__()方法：
    def __getitem__(self, item):
        if isinstance(item, int):  # item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

f = Fib()
print(f[2])
print(f[0 : 5])


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

