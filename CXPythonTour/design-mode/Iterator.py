# coding=utf-8

"""
Created on 2017-11-25
@author: Palesnow

功能：迭代器模式
网址：https://yq.aliyun.com/articles/71068?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13627

"""
# 迭代器抽象类
class Iterator(object):
    def First(self):
        pass
    def Next(self):
        pass
    def Isdone(self):
        pass
    def CurrItem(self):
        pass

# 聚集抽象类:
class Aggregate(object):
    def CreateIterator(self):
        pass

# 具体迭代器类
class ConcreateIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = 0
    def First(self):
        return self.aggregate[0]
    def Next(self):
        ret = None
        if self.curr < len(self.aggregate):
            ret = self.aggregate[self.curr]

        self.curr += 1

        return ret
    def Isdone(self):
        return True if self.curr >= len(self.aggregate) else False
    def CurrItem(self):
        return self.aggregate[self.curr]

# 具体聚集类
class ConcreateAggregate(Aggregate):
    def __init__(self):
        self.ilist = []
    def CreateIterator(self):
        return ConcreateIterator(self)

if __name__ == "__main__":
    ca = ConcreateAggregate()
    ca.ilist.append("first")
    ca.ilist.append("second")
    ca.ilist.append("third")
    ca.ilist.append("four")

    itor = ConcreateIterator(ca.ilist)

    # print(itor.First())
    while not itor.Isdone():
        print(itor.Next())

