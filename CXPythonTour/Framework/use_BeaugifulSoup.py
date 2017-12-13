#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-12
@author: Palesnow

@content: BeautifulSoup使用
@参考资料：http://wiki.jikexueyuan.com/project/python-crawler-guide/beautiful-soup.html

"""
from bs4 import BeautifulSoup
import bs4
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 1、创建beautifulsoup对象
soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(open('index.html'))

# 2、打印soup对象的内容，格式化输出
print(soup.prettify())

'''
四大对象种类
    Tag
    NavigableString
    BeautifulSoup
    Comment

'''
'''
    Tag：就是 HTML 中的一个个标签
    Tag，它有两个重要的属性，是 name 和 attrs
'''
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)
# name
print(soup.name)
print(soup.head.name)
# attrs
print(soup.p.attrs)
# 单独获取某个属性
print(soup.p['class'])
# 利用 get 方法，传入属性的名称
print(soup.p.get('name'))


# 对这些属性和内容等等进行修改
# soup.p['class'] = 'newClass'
# print(soup.p)
# 对这个属性进行删除
# del soup.p['class']
# print(soup.p)


'''
    NavigableString: 可以遍历的字符串
    标签里面的内容,它的类型是一个 NavigableString
'''
# 获取标签内部的文字
print(soup.p.string)
print(type(soup.p.string))

'''
    BeautifulSoup: 表示的是一个文档的全部内容
    大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性
'''
print(type(soup.name))
print(soup.name)
print(soup.attrs)

'''
    Comment: 是一个特殊类型的 NavigableString 对象
    其实输出的内容仍然不包括注释符号，但是如果不好好处理它，
    可能会对我们的文本处理造成意想不到的麻烦
'''
print(soup.a)
print(soup.a.string)  # a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了
print(type(soup.a.string))

if type(soup.a.string) == bs4.element.Comment:
    print(soup.a.string)


'''
    遍历文档树
'''
# 直接子节点: .contents .children 属性
# .contents: tag 的 .content 属性可以将tag的子节点以列表的方式输出
print(soup.head.contents)
print(soup.head.contents[0])

# .children: 它返回的是一个 list 生成器对象，我们可以通过遍历获取所有子节点
print(soup.head.children)
for child in soup.body.children:
    print(child)

# 所有子孙节点：.descendants 属性
# .contents 和 .children 属性仅包含tag的直接子节点，
# .descendants 属性可以对所有tag的子孙节点进行递归循环
print('所有子孙节点')
for child in soup.descendants:
    print(child)

# 节点内容: .string 属性
# 如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容
# 如果 tag 包含了多个子节点,tag 就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print(soup.head.string)
print(soup.title.string)
print(soup.html.string)

# 多个内容: .strings .stripped_strings 属性
# .strings: 获取多个内容，需要遍历获取
for string in soup.strings:
    print(repr(string))
# .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))


# 父节点: .parent 属性
print(soup.p.parent.name)

# 全部父节点: .parents 属性
# 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
content = soup.head.title.string
for parent in content.parents:
    print(parent.name)

# 兄弟节点: .next_sibling .previous_sibling 属性
# 兄弟节点可以理解为和本节点处在统一级的节点，
    # .next_sibling 属性获取了该节点的下一个兄弟节点，
    # .previous_sibling 则与之相反，如果节点不存在，则返回 None
# 实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
    # 因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)

# 全部兄弟节点: .next_siblings .previous_siblings 属性
for sibling in soup.a.next_siblings:
    print(repr(sibling))

# 前后节点: .next_element .previous_element 属性
# 与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
print(soup.head.next_element)
print('------')
print(soup.head.previous_element)

# 所有前后节点: .next_elements .previous_elements 属性
print('------')
for element in soup.head.next_elements:
    print(repr(element))

'''
    搜索文档树
'''
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# 传字符串
print(soup.find_all('b'))
print(soup.find_all('a'))
# 传正则表达式
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)
# 传列表
print(soup.find_all(['a', 'b']))
# 传 True
for tag in soup.find_all(True):
    print(tag.name)
# 传方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))
# keyword 参数
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile('elsie')))
print(soup.find_all(href=re.compile("elsie"), id='link1'))
print(soup.find_all('a', class_='sister'))
# text 参数
print(soup.find_all(text='Elsie'))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))
# limit 参数
print(soup.find_all('a', limit=2))
# recursive 参数
print(soup.html.find_all("title", recursive=False))


'''
    CSS选择器
'''
# 通过标签名查找
print(soup.select('title'))
print(soup.select('a'))

# 通过类名查找
print(soup.select('.sister'))

# 通过 id 名查找
print(soup.select('#link1'))

# 组合查找
print(soup.select('p #link1'))
# 直接子标签查找
print(soup.select('head > title'))

# 属性查找
print(soup.select('a[class="sister"]'))
print(soup.select('p a[href="http://example.com/elsie"]'))
