# coding=utf-8

"""
Created on 2017-11-28
@author: Palesnow

功能：观察者模式
网址：https://yq.aliyun.com/articles/71066?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13629

实例：火警报警器

"""
# ********* 观察者 *************
class Observer:
    def update(self, action):
        pass
# 报警器
class AlarmSensor(Observer):
    def update(self, action):
        print("Alarm Got: %s" % action)
        self.runAlarm()
    def runAlarm(self):
        print("Alarm Ring...")
# 洒水器
class WaterSprinker(Observer):
    def update(self, action):
        print("Sprinker Got: %s" % action)
        self.runSprinker()
    def runSprinker(self):
        print("Spray Water...")
# 拨号器
class EmergencyDialer(Observer):
    def update(self, action):
        print("Dialer Got: %s" % action)
        self.runDialer()
    def runDialer(self):
        print("Dial 119...")

# ********* 被观察者 *************
class Observed:
    observers = []
    action = ""
    def addObserver(self, observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class SmokeSensor(Observed):
    def setAction(self, action):
        self.action = action
    def isFire(self):
        return True

if __name__ == "__main__":
    alarm = AlarmSensor()
    sprinker = WaterSprinker()
    dialer = EmergencyDialer()

    smoke_sensor = SmokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)

    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()
