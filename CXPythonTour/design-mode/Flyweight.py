# coding=utf-8

"""
Created on 2017-11-21
@author: Palesnow

功能：享元模式
网址：https://yq.aliyun.com/articles/70529?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13620

实例：网上咖啡选购平台

"""

# 咖啡类
class Coffee:
    name = ""
    price = 0
    def __init__(self, name):
        self.name = name
        self.price = len(name)
    def show(self):
        print("Coffee Name: %s Price: %s " % (self.name, self.price))

# 咖啡工厂
class CoffeeFactory():
    coffee_dict = {}
    def getCoffee(self, name):
        if (name in self.coffee_dict.keys()) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


# 顾客类
class Customer:
    coffee_factory = ""
    name = ""
    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory
    def order(self, coffee_name):
        print("%s ordered a cup of coffee: %s" % (self.name, coffee_name))
        return self.coffee_factory.getCoffee(coffee_name)


if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    customer_2 = Customer("B Client", coffee_factory)
    customer_3 = Customer("C Client", coffee_factory)
    customer_4 = Customer("D Client", coffee_factory)

    c1_capp = customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha = customer_2.order("mocha")
    c2_mocha.show()
    c3_capp = customer_3.order("cappuccino")
    c3_capp.show()
    c4_capp = customer_4.order("cappuccino")
    c4_capp.show()

    print("Num of Coffee Instance: %s" % coffee_factory.getCoffeeCount())