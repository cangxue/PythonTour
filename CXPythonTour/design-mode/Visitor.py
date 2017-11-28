# coding=utf-8

"""
Created on 2017-11-24
@author: Palesnow

功能：访问者模式
网址：https://yq.aliyun.com/articles/71075?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13628

实例：药房业务系统

"""

# 药品类
class Medicine:
    name = ""
    price = 0.0
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def accept(self, visitor):
        pass
# 抗生素
class Antibiotic(Medicine):
    def accept(self, visitor):
        visitor.visit(self)
# 感冒药
class Coldrex(Medicine):
    def accept(self, visitor):
        visitor.visit(self)

# 工作人员类
class Visitor:
    name = ""
    def setName(self, name):
        self.name = name
    def visit(self, medicine):
        pass
# 药品划价员
class Charger(Visitor):
    def visit(self, medicine):
        print("CHARGER: %s lists the Medicine %s. Price: %s" % (self.name, medicine.getName(), medicine.getPrice()))
# 药房管理员
class Pharmacy(Visitor):
    def visit(self, medicine):
        print("PHARMACY: %s offers the Medicine %s. Price: %s" % (self.name, medicine.getName(), medicine.getPrice()))

# 药方类
class ObjectStructure:
    pass
class Prescription(ObjectStructure):
    medicines = []
    def addMedicine(self, medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self, medicine):
        self.medicines.remove(medicine)
    def visit(self, visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__ == "__main__":
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Pencillin", 3.0)

    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)

    charger = Charger()
    charger.setName("Doctor Strange")
    pharger = Pharmacy()
    pharger.setName("Doctor Wei")

    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharger)

