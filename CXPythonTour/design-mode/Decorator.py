# coding=utf-8

"""
Created on 2017-11-17
@author: Palesnow

功能：装饰器模式
网址：https://yq.aliyun.com/articles/70737?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11966

"""

# 饮料类
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0
class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

# 装饰器类
class drinkDecorator(Beverage):
    def getName(self):
        pass
    def getPrice(self):
        pass
class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    def getName(self):
        return self.beverage.getName() + " + ice"
    def getPrice(self):
        return self.beverage.getPrice() + 0.3

class sugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    def getName(self):
        return self.beverage.getName() + " + sugar"
    def getPrice(self):
        return self.beverage.getPrice() + 0.5

if __name__ == "__main__":
    coke_cola = coke()
    print("Name: %s" % coke_cola.getName())
    print("Price: %s" % coke_cola.getPrice())

    ice_coke = iceDecorator(coke_cola)
    print("Name: %s" % ice_coke.getName())
    print("Price: %s" % ice_coke.getPrice())