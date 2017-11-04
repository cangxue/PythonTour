# coding=utf-8

"""
Created on 2017-11-03
@author: Palesnow

功能：单例模式实现
网址：https://yq.aliyun.com/articles/70418?spm=5176.100239.blogcont70448.17.Y8DcR1

"""

import threading
import time

# 这里使用方法__new__来实现单例模式
class Singleton(object): # 抽象单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance