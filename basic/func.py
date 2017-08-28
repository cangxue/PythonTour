import math

x = input('a=')
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(x))


a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
def quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if delta >= 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*1)
            return x1, x2
        else:
            return 'b的平方是小于4ac的不行哦'
    else:
        return 'a,b,c不全为数值'

print('解为',quadratic(a,b,c))
        

