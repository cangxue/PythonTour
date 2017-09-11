#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误调试
# 1、print()把可能有问题的变量打印出来
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

# main()

# 2、用断言（assert）来替代,如果断言失败，assert语句本身就会抛出AssertionError：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()

# 3、logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

# 4、pdb.set_trace()
import pdb
s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)