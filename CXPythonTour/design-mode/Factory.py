# coding=utf-8

"""
Created on 2017-11-07
@author: Palesnow

功能：工厂模式
网址：https://yq.aliyun.com/articles/70417?spm=5176.100239.blogcont70418.16.8afBLL

"""

#************ 产品类 **************#
# 抽象产品类
class Button():
    def display(self):
        print("显示button")
# 具体产品类
class RedButton(Button):
    def display(self):
        print("显示红色button")
class GreenButton(Button):
    def display(self):
        print("显示绿色button")

# 抽象产品类
class TextField():
    def display(self):
        print("显示textfield")
# 具体产品类
class RedTextField(TextField):
    def display(self):
        print("显示红色textfield")
class GreenTextField(TextField):
    def display(self):
        print("显示绿色textfield")

#************ 工厂类 **************#
# 简单工厂模式
class SimpleFactory():
    @classmethod
    def create(cls, factoryClass):
        factoryIns = factoryClass()
        return factoryIns

# 工厂模式
class Factory():
    def create(self, factoryClass):
        factoryIns = factoryClass()
        return factoryIns

# 抽象工厂模式
class AbstractFactory():
    def createButton(self, factoryClass):
        factoryIns = factoryClass()
        return factoryIns

    def createTextField(self, factoryClass):
        factoryIns = factoryClass()
        return factoryIns

class AbstractRedFactory(AbstractFactory):
    def createButton(self):
        button = RedButton()
        return button
    def createTextField(self):
        textField = RedTextField()
        return textField

class AbstractGreenFactory(AbstractFactory):
    def createButton(self):
        button = GreenButton()
        return button
    def createTextField(self):
        textField = GreenTextField()
        return textField

class FactoryProducer:
    def getFactory(self, factoryClass):
        factoryIns = factoryClass()
        return factoryIns

# ************ 使用工厂 **************#
if __name__ == "__main__":
    # 简单工厂模式
    simple_button = SimpleFactory.create(RedButton)
    simple_button.display()

    # 工厂模式
    factory = Factory()
    button = factory.create(GreenButton)
    button.display()

    # 抽象工厂模式
    abstract_factory = FactoryProducer().getFactory(AbstractGreenFactory)
    redbutton = abstract_factory.createButton()
    redbutton.display()
    redTextField = abstract_factory.createTextField()
    redTextField.display()
