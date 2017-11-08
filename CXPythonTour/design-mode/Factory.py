# coding=utf-8

"""
Created on 2017-11-07
@author: Palesnow

功能：工厂模式
网址：https://yq.aliyun.com/articles/70417?spm=5176.100239.blogcont70418.16.8afBLL

"""

# 快餐点餐系统
# 主餐生成
class Burger(): # 抽象产品类
    name = ""
    price = 0.0
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class cheeseBurger(Burger): # 具体产品类
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0
class spicyChickenBurger(Burger): # 具体产品类
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0

# 小食
class Snack(): # 抽象产品类
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class chips(Snack): # 具体产品类
    def __init__(self):
        self.name = "chips"
        self.price = 6.0
class chickenWings(Snack): # 具体产品类
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

# 饮料
class Beverage(): # 抽象产品类
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class coke(Beverage): # 具体产品类
    def __init__(self):
        self.name = "coke"
        self.price = 4.0
class milk(Beverage): # 具体产品类
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


# 工厂
class foodFactory(): # 抽象产品类
    type = ""
    def createFood(self, foodClass):
        print(self.type, "factory produce a instance.")
        foodIns = foodClass()
        return foodIns
class burgerFactory(foodFactory): # 具体产品类
    def __init__(self):
        self.type = "BURGER"
class snackFactory(foodFactory): # 具体产品类
    def __init__(self):
        self.type = "SNACK"
class beverageFactory(foodFactory): # 具体产品类
    def __init__(self):
        self.type = "BEBERAGE"


# 生产产品
if __name__ == "__main__":
    burger_factory = burgerFactory()
    snack_factory = snackFactory()
    beverage_factory = beverageFactory()

    cheese_burger = burger_factory.createFood(cheeseBurger)
    print(cheese_burger.getName(), cheese_burger.getPrice())

    chicken_wings = snack_factory.createFood(chickenWings)
    print(chicken_wings.getName(), chicken_wings.getPrice())

    coke_drink = beverage_factory.createFood(coke)
    print(coke_drink.getName(), coke_drink.getPrice())

