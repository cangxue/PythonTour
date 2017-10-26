
# 常量

# 数
a1 = 2
a2 = 23.4E-4
a3 = (-5+4j)
print(a1, a2, a3.real)

# 字符串
b1 = '''This is a multi-line string. "What's your name?" ;'i asked' '''
print(b1)

# escape character/转义符
b2 = 'What\'s your name?'
b3 = '用转义符 \\来指示反斜杠本身'
b4 = "This is the first sentence.\
This is the second sentence."
print(b2, b3, b4)

# 变量
i = 5
print(i)


print('I\'m \"ok\"!')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')

# bool
print(3 > 2)
print(5 > 3 and 3 > 2)
print(5 > 3 or 3 > 4)
print(not 1 > 2)

# None

# variable
a = 10
t_007 = 'T007'
Answer = True
print(a, t_007, Answer)

x = 10
x = x + 2
print(x)

b = a
a = 20
print(a, b)

# 通常用全部大写的变量名表示常量
PI = 3.14159265359

# 除法
# 一种除法是/：
print(10/3, 9/3)
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10 // 3)
print(10 % 3)
print(3**4)
# 2 ->10 <<2 1000 -> 2**3 = 8
# 11 -> 1011 >> 0101 -> 1 + 2*2 = 5
print(2 << 2, 11 >> 1)
# 5 -> 101
# 7 -> 111
# 5 | 7 = 111 = 7 或
# 5 & 7 = 101 = 5 与
# 5 ^ 7 = 010 000 = 10 = 2 异或
print(5 | 7, 5 & 7, 5 ^ 7)
# Unicode
print('包含中文的str')
# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'), ord('中'), chr(66), chr(25991))
print('\u4e2d\u6587')
print(len('ABC'),len('中文'.encode('utf-8')), len(b'ABC'))

b = 'name: %s, age: %d, height: %.2f' % ('palesnow', 26, 183.3)
print(b)


f = int(4.6)
h = int(4.2)
print(f, h)

f1 = float(2)
print(f1)

#复数
c = complex(4)
print(c)

z = 1.23e-4 + 5.4e-1 + 89j
print(z.real, z.imag)
