# coding=utf-8

"""
Created on 2017-11-28
@author: Palesnow

功能：MVC模式

实例：学生信息打印

"""
# Model
class Student():
    name = ""
    age = 0

    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

# View
class StudentView():
    def printStudentDetails(self, studentName, studentAge):
        print("%s age is %d" % (studentName, studentAge))

# Controller
class StudentController():
    model = None
    view = None
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def setStudentName(self, name):
        self.model.setName(name)
    def getStudentName(self):
        return self.model.getName()
    def setStudentAge(self, age):
        self.model.setAge(age)
    def getStudentAge(self):
        return self.model.getAge()

    def updateView(self):
        self.view.printStudentDetails(self.getStudentName(),self.getStudentAge())

if __name__ == "__main__":
    model = Student()
    model.setName("Robert")
    model.setAge(10)

    view = StudentView()

    controller = StudentController(model, view)
    controller.updateView()

    controller.setStudentName("PaleSnow")
    controller.updateView()