
#if elif
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
elif bmi >= 28 and bmi <=32:
    print('童鞋你该减肥啦！')
else :
    print('童鞋你长得很圆吧！')

#for  in
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
