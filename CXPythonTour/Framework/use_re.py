#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-12
@author: Palesnow

@content: re模块使用
@参考资料：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

"""

import re

# 转义问题处理
# 使用Python的r前缀，就不用考虑转义的问题
print('abc\\-001')
print(r'abc\-001')

# 正则表达式匹配
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

test = '010-12345'
regex = r'^\d{3}\-\d{3,8}$'
if re.match(regex, test):
    print('ok')
else:
    print('failed')

# 切分字符串
test = 'a b  c'
print(test.split(' '))
print(re.split(r'\s+', test))
test = 'a,b;; c   d'
print(re.split(r'[\s\,\;]+', test))

# 分组
# 用()表示的就是要提取的分组（Group)
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-1234567')
print(m)
print(m.group(0))  # 永远是原始字符串
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# 编译
"""
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：

    编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

    用编译后的正则表达式去匹配字符串。
"""
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())


# 操作方法
'''
    compile(pattern, flags=0)
    pattern: 可以理解为一个匹配模式
    re.compile: 获得一个匹配模式
'''
'''
    match(pattern, string, flags=0)
    将会从 string（我们要匹配的字符串）的开头开始，尝试匹配 pattern，一直向后匹配，
    如果遇到无法匹配的字符，立即返回 None，
    如果匹配未结束已经到达 string 的末尾，也会返回 None。
    
    match 对象的的属性和方法
    属性：
    1.string: 匹配时使用的文本。
    2.re: 匹配时使用的Pattern对象。
    3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    5.lastindex: 最后一个被捕获的分组在文本，中的索引。如果没有被捕获的分组，将为None。
    6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

'''
pattern = re.compile(r'hello')
print(re.match(pattern, 'hello'))
print(re.match(pattern, 'helloo pale'))
print(re.match(pattern, 'helo pale'))


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
m = re_telephone.match('010-12345')
print(m.endpos, m.lastindex, m.lastgroup)

# 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回
print(m.group(), m.group(1, 2))
# 以元组形式返回全部分组截获的字符串
print(m.groups())
# 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内
m1 = re.match(r"(?P<first>\w+) (?P<second>\w+)", "Malcolm Reynolds")
print(m1.groupdict())
# 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引)
print(m.start(2))
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1)
print(m.end(2))
# 返回(start(group), end(group))
print(m.span(2))
# 将匹配到的分组代入template中然后返回
print(m.expand(r'\2 \2 \1'))

'''
    search(pattern, string, flags=0)
    search 方法与 match 方法极其类似，区别在于 
    match() 函数只检测 re 是不是在 string的开始位置匹配，
    search() 会扫描整个 string 查找匹配，
    match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match() 就返回 None。
    同样，search 方法的返回对象同 match() 返回对象的方法和属性。
'''
pattern = re.compile(r'world')
match = re.search(pattern, 'hello world!')
print(match.group())

'''
    split(pattern, string, maxsplit=0, flags=0):
    按照能够匹配的子串将 string 分割后返回列表。
    maxsplit 用于指定最大分割次数，不指定将全部分割。
'''
pattern = re.compile(r'\d+')
print(re.split(pattern, 'one1two2three3four4', maxsplit=0))

'''
    findall(pattern, string, flags=0):
    搜索 string，以列表形式返回全部能匹配的子串
'''
pattern = re.compile(r'\d+')
print(re.findall(pattern, 'one1two2three3four4'))

'''
    finditer(pattern, string, flags=0)
    搜索 string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
'''
pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print(m.group())

'''
    sub(pattern, repl, string, count=0, flags=0):
    使用 repl 替换 string 中每一个匹配的子串后返回替换后的字符串。 
    当 repl 是一个字符串时，可以使用 \id 或 \g、\g 引用分组，但不能使用编号0。 
    当 repl 是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
    count 用于指定最多替换次数，不指定时全部替换。
'''
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.sub(pattern, r'\2 \1', s))

def fun(m):
    return m.group(2).title() + ' ' + m.group(1).title()
print(re.sub(pattern, fun, s))

'''
    subn(pattern, repl, string, count=0, flags=0):
    返回 (sub(pattern, repl, string, count=0, flags=0), 替换次数)
'''
print(re.subn(pattern, fun, s))