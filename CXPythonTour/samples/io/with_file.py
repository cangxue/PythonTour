#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是： ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

# 标示符'r'表示读
with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

# 十六进制表示的字节
with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)


# 内存中读写
# 字符串
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())

# 二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())