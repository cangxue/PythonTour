# coding=utf-8

"""
Created on 2017-11-21
@author: Palesnow

功能：组合模式
网址：https://yq.aliyun.com/articles/70535?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11422

实例：公司组织结构

"""

class Company:
    name = ''
    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass
    def remove(self, company):
        pass
    def display(self, depth):
        pass
    def listDuty(self):
        pass

class ConcreteCompany(Company):
    childrenCompany = None
    def __init__(self, name):
        Company.__init__(self, name)
        self.childrenCompany = []
    def add(self, company):
        self.childrenCompany.append(company)
    def remove(self, company):
        self.childrenCompany.remove(company)
    def display(self, depth):
        print("-"*depth + self.name)
        for component in self.childrenCompany:
            component.display(depth + 1)
    def listDuty(self):
        for component in self.childrenCompany:
            component.listDuty()
# HR
class HRDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)
    def display(self, depth):
        print("-"*depth + self.name)
    def listDuty(self):  # 履行职责
        print('%s\t Enrolling & Transfering management.' % self.name)

# Finance
class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)
    def display(self, depth):
        print("-" * depth + self.name)
    def listDuty(self):
        print("%s\t Finance Management." % self.name)

# RD
class RdDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)
    def display(self, depth):
        print("-"*depth + self.name)
    def listDuty(self):
        print("%s\t Research & Development." % self.name)


if __name__ == "__main__":
    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment("HQ R&D"))

    comp = ConcreteCompany('East Branch')
    comp.add(HRDepartment('East.Br HR'))
    comp.add(FinanceDepartment('East.Br Finance'))
    comp.add(RdDepartment("East.Br R&D"))
    root.add(comp)

    comp1 = ConcreteCompany('Northast Branch')
    comp1.add(HRDepartment('Northeast.Br HR'))
    comp1.add(FinanceDepartment('Northeast.Br Finance'))
    comp1.add(RdDepartment("Northeast.Br R&D"))
    comp.add(comp1)

    comp2 = ConcreteCompany('Southeast Branch')
    comp2.add(HRDepartment('Southeast.Br HR'))
    comp2.add(FinanceDepartment('Southeast.Br Finance'))
    comp2.add(RdDepartment("Southeast.Br R&D"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()