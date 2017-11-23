# coding=utf-8

"""
Created on 2017-11-23
@author: Palesnow

功能：责任链模式
网址：https://yq.aliyun.com/articles/71074?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13623

实例：请假系统

"""
# 请假类
class Request():
    requestType = ""
    requestContent = ""
    number = 0

# 抽象经理类
class Manager():
    successor = None
    name = ""
    def __init__(self, name):
        self.name = name
    def setSuccessor(self, successor):
        self.successor = successor
    def handleRequest(self, request):
        pass
# 直属经理
class LineManager(Manager):
    def handleRequest(self, request):
        if request.requestType == "DayOff" and request.number <= 3:
            print("%s:%s Num:%d Accepted OVER" % (self.name, request.requestContent, request.number))
        else:
            print("%s:%s Num:%d Accepted CONTINUE" % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)
# 部门经理
class DepartmentManager(Manager):
    def handleRequest(self, request):
        if request.requestType == "DayOff" and request.number <= 7:
            print("%s:%s Num:%d Accepted OBER" % (self.name, request.requestContent, request.number))
        else:
            print("%s:%s Num:%d Accepted CONTINUE" % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)
# 总经理
class GeneralManager(Manager):
    def handleRequest(self, request):
        if request.requestType == "DayOff":
            print("%s:%s Num:%d Accepted OVER" % (self.name, request.requestContent, request.number))


if __name__ == "__main__":
    line_manager = LineManager("LINE MANAGER")
    department_manager = DepartmentManager("DEPARTMENT MANAGER")
    general_manager = GeneralManager("GENERAL MANAGER")

    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = Request()
    req.requestType = "DayOff"
    req.requestContent = "Ask 1 day off"
    req.number = 1
    line_manager.handleRequest(req)

    print("===============")
    req.requestContent = "Ask 5 day off"
    req.number = 5
    line_manager.handleRequest(req)

    print("===============")
    req.requestContent = "Ask 10 day off"
    req.number = 10
    line_manager.handleRequest(req)
