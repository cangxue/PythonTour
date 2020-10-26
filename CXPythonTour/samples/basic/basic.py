# String

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

message = "  python "
print(message)
print(message.rstrip())

# Number
a = 2 + 3
print(a)

b = 0.2 + 0.1
print(b)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 进制问题
# 十进制转二进制
bin(10)
# 十进制转八进制
oct(9)
# 十进制转十六进制
hex(15)

# 商和余数
divmod(10, 3)
# 幂和余同时做
pow(3, 2, 4)
# 四舍五入
round(10.0012, 2)

# 1 保留小数点后两位
print("{:.2f}".format(3.1415926))