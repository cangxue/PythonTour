# 切片 Slice
# 创建一个0-99的数列：
L = list(range(100))
# 前十个
print(L[:10])
# 后十个
print(L[-10:])
# 前11 - 20个
print(L[10:20])
# 前十个数，每两个取
print(L[:10:2])
# 所有数，每5个取
print(L[::5])

# tuple
t = (1, 2, 3, 4, 5)
print(t[:3])
t2 = tuple(range(50))
print(t2[25:35])

# string
s = 'ASDFGH'
print(s[-3:])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)

for ch in 'ABc':
    print(ch)

# from collections import Iterable
# isinstance('abc', Iterable) # str是否可迭代

# 获取索引
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

for x, y in enumerate([(2, 3), (3, 3), (4, 4)]):
    print(x, y)

for x, y, z in [(1, 1, 3), (2, 4, 5), (3, 9, 7)]:
    print(x, y, z)

# 列表生成式
l1 = list(range(1, 11))
print(l1)
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 生成的元素x * x放到前面，后面跟for循环
l2 = [x * x for x in range(1, 11)]
print(l2)

l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)

l4 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)

l5 = [m + n + o for m in 'AB' for n in 'EF' for o in 'XY']
print(l5)

# 列出当前目录下的所有文件和目录名，
import os
l6 = [d for d in os.listdir('.')]
print(l6)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
# 使用两个变量来生成list
l7 = [k + '=' + v for k, v in d.items()]
print(l7)

# 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
l8 = [s.lower() for s in L]
print(l8)

L = ['Hello', 'World', 18, 'IBM', 'Apple']
l9 = [s.lower() for s in L if isinstance(s, str)]
l10 = [s.lower() for s in L if type(s) == str]
print(l9)
print(l10)

# 语法：isinstance（object，type）
# 作用：来判断一个对象是否是一个已知的类型。


# 生成器：generator，这种一边循环一边计算的机制，称为生成器
# 方法一
L = [x * x for x in range(10)]  # list
print(L)
g = (x * x for x in range(10))  # generator
for n in g:
    print(n)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
# genarator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
l = fib(6)
for n in l:
    print(n)

# 最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
l = odd()
for n in l:
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Cenerator return value:', e.value)
        break

# 杨辉三角
# 方法一
def triangles():
    L = [1]
    while True: #一直循环生成无限临时数据
        yield L
        L = [L[i-1] + L[i] for i in range(1, len(L))]
        L.insert(0, 1)
        L.append(1)
n = 0
for x in triangles():
    print(str.center(str(x), 50, " "))
    n += 1
    if n == 10:
        break

# 方法二
def triangles(lines):
    L = [1]
    n = 0
    while n < lines:
        yield L
        L1 = [1]
        for i in range(0, len(L) - 1):
            L1.append(L[i] + L[i + 1])
        L1.append(1)
        L = L1
        n = n + 1

for t in triangles(10):
    print(t)
    n = n + 1
    if n == 10:
        break


# 迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
# from collections import Iterator
# isinstance((x for x in range(10)), Iterator)

# 可以使用isinstance()判断一个对象是否是Iterable对象：
# from collections import Iterable
# isinstance([], Iterable)

# 生成器都是Iterator对象，
# 但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# isinstance(iter([]), Iterator)

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，
# 它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，
# 不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    print(x)
    pass
# 实际上完全等价于：
# 首先获得Iterator对象；
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        print('循环结束了')
        break

