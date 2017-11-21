# coding=utf-8

"""
Created on 2017-11-21
@author: Palesnow

功能：门面模式
网址：https://yq.aliyun.com/articles/70532?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11968

实例：警报系统
"""

# 警报器
class AlarmSensor:
    def run(self):
        print("Alarm Ring...")
# 喷水器
class WaterSprinker:
    def run(self):
        print("Spray Water...")
# 自动拨打电话
class EmergencyDialer:
    def run(self):
        print("Dial 119...")

# 门面
class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()

if __name__ == "__main__":
    emergency_facade = EmergencyFacade()
    emergency_facade.runAll()



