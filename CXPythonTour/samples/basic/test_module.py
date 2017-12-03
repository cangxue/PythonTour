#!/user/bin/env python3
# _*_ coding: utf-8 _*_


def addFunc(a, b):
    return a + b

# 让模块既可以导入到别的模块中用，另外该模块自己也可执行。
#
# 注：name两边各有2个下划线__name__有2个取值：
# 当模块是被调用执行的，取值为模块的名字；
# 当模块是直接执行的，则该变量取值为：__main__
if __name__ == '__main__':

    print('test_module 计算结果:', addFunc(1, 1))
