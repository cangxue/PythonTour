# if elif
s = input('age:')
age = int(s)
if age >= 60:
    print('old')
elif age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

height = input('height:')
weight = input('weight:')

bmi = float(weight) / float(height)**2
print(bmi)
if bmi < 18.5:
    print('童鞋你太瘦啦！')
elif bmi >= 18.5 and bmi <= 25:
    print('童鞋你身材很棒哦！')
elif bmi >= 25 and bmi <= 28:
    print('童鞋你超重了喔！')
elif bmi >= 28 and bmi <= 32:
    print('童鞋你该减肥啦！')
else:
    print('童鞋你长得很圆吧！')

# for  in
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

# break：提前退出循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue：跳过当前的这次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')

# if arr is None:
#     pass
# if arr is not None:
#     pass

# try:
#     val = d['c']
# except KeyError:
#     print('c' not existence)

# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (j, i, j * i), end="\t")
    print()

[1, 2, 3][::-1]
