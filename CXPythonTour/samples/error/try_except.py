#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误处理

# try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        print('try...')
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()


# 调用堆栈
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# main()

# 记录错误
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# main()
print('END')

# 但程序打印完错误信息后会继续执行，并正常退出：

# 自定义错误类
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

# 错误类型转换
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')