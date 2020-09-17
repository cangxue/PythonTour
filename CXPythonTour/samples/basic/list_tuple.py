
# list
classmates = ['Michael', 'Bob', 'Tracy']
a = len(classmates)
b = classmates[1]
# 用-1做索引，直接获取最后一个元素
c = classmates[-1]
d = classmates[-2]
print(a, b, c, d)

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
# 要删除list末尾的元素，用pop()方法
classmates.pop()
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'

# 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# list里面的元素的数据类型也可以不同
l1 = ['Apple', 123, True]
l2 = ['python', 'java', l1, 'scheme']
print(l2)

e = l2[2][1]
print(e) # 123

# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

for value in range(1,5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

numbers = list(range(2, 11, 2))
print(numbers)

squares = []
for value in range(1,10):
	square = value**2
	squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares2[value**2 for value in range(1,11)]
print(squares2)

# tuple
t = (1, 2)
print(t)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t1 = (1,)

t2 = ('a', 'b', ['A', 'B'])
print(t2)
t2[2][0] = 'X'
t2[2][1] = 'Y'
print(t2)

#字符串使用实例
months = 'JanFebMarAprMayJunJulAugSepOctNovDes'
n = input('请输入月份数（1-12）：')
pos = (int(n) - 1) * 3
monthAbbrev = months[pos: pos+3]
print('月份简写是：' + monthAbbrev + '.')