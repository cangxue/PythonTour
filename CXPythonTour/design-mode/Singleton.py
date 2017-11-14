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

# 总线
class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...", data)
        self.lock.release()
# 线程对象，为更加说明单例的含义，将Bus对象实例化写在run里
class VisitEntity(threading.Thread):
    my_bus = ''
    name = ''
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run..." %i)
        my_entity = VisitEntity()
        my_entity.setName("entity_" + str(i))
        my_entity.start()