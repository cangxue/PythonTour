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


# filter
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
print(L)

# 删除空字符串
def not_empty(s):
    return s and s.strip()
L = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# print(L)

# 取素数
# 1.这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

# 2.定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0

# 3.定义一个生成器，不断返回下一个素数：
def primes():
    yield 2;
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 4.打印100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# 回数
def is_same(n):
    a = str(n)
    num = len(a)
    result = True
    for i in range(0, (num + 1) // 2):
        if a[i] != a[num - 1 - i]:
            result = False
    return result
L = list(filter(is_same, range(900, 1000)))
# print(L)


# sorted
L = [36, 5, -12, 9, -21]
print(sorted(L))
# 绝对值大小排序
print(sorted(L, key=abs))

L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))

print(sorted(L, key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(L, key=str.lower, reverse=True))

# 成绩排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L1 = sorted(L, key=by_name)
print(L1)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)


# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1, 3, 4, 5))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 4, 5)
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构
print(f())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count()
print(f4(), f5(), f6())

L = count() # 返回的是个函数list
print(L[0](), L[1](), L[2]())


# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
L = list(map(lambda x: x * x, [1, 2, 3]))
print(L)

f = lambda x: x + x
print(f(5))

# 匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
print(build(4, 5)())

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2017-9-7')

f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(f.__name__)

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2017-9-7-4-57')

now()

@log
def build(x, y):
    return lambda: x * x + y * y
print(build(4, 5)())

# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-9-7-4-57')

now()
print(now.__name__)

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute22')
def now():
    print('2017-9-7-4-57')

now()
print(now.__name__)

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现

def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # try:
            #     print('%s %s %s():' % ('begin', text, func.__name__))
            #     return func(*args, **kw)
            # finally:
            #     print('%s %s %s():' % ('end', text, func.__name__))

            print('%s %s %s():' % ('begin', text, func.__name__))
            func(*args, **kw)
            print('%s %s %s():' % ('end', text, func.__name__))
        return wrapper
    return decorator

@log()
def now1():
    print('2017-9-7')

@log('execute')
def now2():
    print('2017-9-7')

now1()
now2()



# 偏函数

print(int('12345'))
print(int('12345', base=8))

def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))

int3 = functools.partial(int, base=2)
print(int3('1010101'))
# functools.partial就是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
