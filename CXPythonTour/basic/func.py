
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

y = int(input('age'))
print(my_abs(y))


def quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if not  isinstance(a, (int, float)) and not isinstance(b, (int, float)) and not isinstance(c, (int, float)):
        raise TypeError('请输入正确的系数')
    if delta >= 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return x1, x2
    else:
        return '无解，b的平方是小于4ac的'

x = float(input('请输入2次项系数a'))
y = float(input('请输入1次项系数b'))
z = float(input('请输入常数项系数c'))
print('解为：', quadratic(x,y,z))

