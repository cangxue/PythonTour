#! * coding: utf-8 *

# 高阶函数

# 变量可以指向函数

x = abs(-10)
print(x)

# 函数本身赋值给变量
f = abs
print(f(-9))

# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。


# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式.
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


# map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x

r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add(x, y):
    return x + y
z = reduce(add, [1, 3, 5, 7, 9])
print(z)

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [2, 4, 6, 8]))

# 把字符串转化为整数
def str_int(s):
    def char_num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char_num, s))

print(str_int('12345'))

def normalize(name):
    first = name[0].upper()
    name = name.lower()[1:]
    return first + name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def str_float(s):
    def fx(x, y):
        return x / 10 + y
    def char_num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    L = s.split('.',1)
    return reduce(fn, map(char_num, L[0])) + reduce(fx, map(char_num, L[1][-1::-1]))/10
print('123.456')
