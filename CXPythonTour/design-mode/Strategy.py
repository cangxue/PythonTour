# coding=utf-8

"""
Created on 2017-11-23
@author: Palesnow

功能：策略模式
网址：https://yq.aliyun.com/articles/71071?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13622

实例：客户消息通知

"""

# 客户类
class Customer:
    customer_name = ""
    info = ""
    phone = ""
    email = ""
    send_way = ""
    def setPhone(self, phone):
        self.phone = phone
    def getPhone(self):
        return self.phone
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email
    def setInfo(self, info):
        self.info = info
    def setName(self, name):
        self.customer_name = name
    def setBrdWay(self, send_way):
        self.send_way = send_way
    def sendMsg(self):
        self.send_way.send(self.info)

# 发送方法
class MsgSender:
    dst_code = ""
    def setCode(self, code):
        self.dst_code = code
    def send(self, info):
        pass
class EmailSender(MsgSender):
    def send(self, info):
        print("EMAIL_ADDRESS: %s EMAIL: %s" % (self.dst_code, info))
class TextSender(MsgSender):
    def send(self, info):
        print("TEXT_CODE: %s TEXT: %s" % (self.dst_code, info))

if __name__ == "__main__":
    customer_x = Customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("123456")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party")

    email_sender = EmailSender()
    email_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(email_sender)
    customer_x.sendMsg()

    text_sender = TextSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sendMsg()