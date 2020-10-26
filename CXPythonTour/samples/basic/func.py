from math import *


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('请输入正确的年龄')

    if x > 70:
        return '你老了'
    elif x > 30:
        return '你成年了'
    else:
        return '小孩别闹'


# y = int(input('age'))
# print(my_abs(y))


def quadratic(a, b, c):
    delta = b**2 - 4 * a * c
    if not isinstance(a, (int, float)) and not isinstance(
            b, (int, float)) and not isinstance(c, (int, float)):
        raise TypeError('请输入正确的系数')
    if delta >= 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return x1, x2
    else:
        return '无解，b的平方是小于4ac的'


# x = float(input('请输入2次项系数a'))
# y = float(input('请输入1次项系数b'))
# z = float(input('请输入常数项系数c'))
# print('解为：', quadratic(x,y,z))


# 初始值
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')

    return L


print(add_end(), add_end([1, 2, 3]))


# 可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4))

# 把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))
print(calc(*(1, 2, 3)))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
# *后面的参数被视为命名关键字参数。
# 命名关键字参数必须传入参数名
# 使用命名关键字参数时，要特别注意，如果没有可变参数，
# 就必须加一个*作为特殊分隔符。如果缺少*，
# Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Bob', 35, 33, city='Beijing', job='Engineer')


# 参数组合
# 必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
def f1(a, b, c=0, *arga, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'arga=', arga, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1), fact(5))


# 尾递归
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))


# 汉诺塔：2^n – 1
# 若n为偶数，按顺时针方向依次摆放 A B C
# 若n为奇数，按顺时针方向依次摆放 A C B。
def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
        return
    else:
        pass

    if n % 2 == 1:
        move(n - 2, a, b, c)
        print('%s --> %s' % (a, b))
        move(n - 2, c, a, b)
        print('%s --> %s' % (a, c))
        move(n - 2, b, c, a)
        print('%s --> %s' % (b, c))
        return move(n - 2, a, b, c)
    else:
        move(n - 1, a, c, b)
        print('%s --> %s' % (a, c))
        return move(n - 1, b, a, c)


move(2, 'A', 'B', 'C')


def func1():
    global x

    print('x is', x)
    x = 2
    print('changed local x to', x)


x = 50
func1()
print('value of x is', x)

#
print(divmod(13, 5))
# 返回（2，3）


def foo(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(nums)
    return evens


foo([10, 2, 4, 5, 7])


def foo(length, width, height=1.0):
    return length * width * height
