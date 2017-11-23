# coding=utf-8

"""
Created on 2017-11-23
@author: Palesnow

功能：命令模式
网址：https://yq.aliyun.com/articles/71070?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13624

实例：饭店点餐系统

"""

"""
接收者
"""
# 后台系统
class backSys():
    def cook(self, dish):
        pass
class mainFoodSys(backSys):
    def cook(self, dish):
        print("MAINFOOD: Cook %s" % dish)
class coolDishSys(backSys):
    def cook(self, dish):
        print("COOLDISH: Cook %s" % dish)
class hotDishSys(backSys):
    def cook(self, dish):
        print("HOTDISH: Cook %s" % dish)

"""
调用者
"""
# 前台服务员系统
class waiterSys():
    commandList = []
    def setOrder(self, command):
        print("WAITER: Add dish")
        self.commandList.append(command)

    def cancelOrder(self, command):
        print("WAITER: Cancel order...")
        self.commandList.remove(command)

    def notify(self):
        print("WAITER: Notify...")
        for command in self.commandList:
            command.execute()

"""
命令类
"""
# 抽象命令类
class Command():
    receiver = None
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        pass
class foodCommand(Command):
    dish = ""
    def __init__(self, receiver, dish):
        self.receiver = receiver
        self.dish = dish
    def execute(self):
        self.receiver.cook(self.dish)
# 具体命令类
class mainFoodCommand(foodCommand):
    pass
class coolDishCommand(foodCommand):
    pass
class hotDishCommand(foodCommand):
    pass

# 菜单类
class menuAll:
    menu_map = dict()
    def loadMenu(self):
        self.menu_map["hot"] = ["Yu-Xiang Sharedded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]
    def isHot(self, dish):
        if dish in self.menu_map["hot"]:
            return True
        return False
    def isCool(self, dish):
        if dish in self.menu_map["cool"]:
            return True
        return False
    def isMain(self, dish):
        if dish in self.menu_map["main"]:
            return True
        return False


# 业务场景
if __name__ == "__main__":
    # 顾客点的菜
    dish_list = ["Yu-Xiang Sharedded Pork", "Sauteed Tofu, Home Style", "Cucumber", "Rice"]

    # 调用者
    waiter_sys = waiterSys()

    # 接收者
    main_food_sys = mainFoodSys()
    cool_dish_sys = coolDishSys()
    hot_dish_sys = hotDishSys()

    menu = menuAll()
    menu.loadMenu()

    # 命令者
    for dish in dish_list:
        if menu.isCool(dish):
            cmd = coolDishCommand(cool_dish_sys, dish)
        elif menu.isHot(dish):
            cmd = hotDishCommand(hot_dish_sys, dish)
        elif menu.isMain(dish):
            cmd = mainFoodCommand(main_food_sys, dish)
        else:
            continue

        waiter_sys.setOrder(cmd)

    waiter_sys.notify()










