# coding=utf-8

"""
Created on 2017-11-24
@author: Palesnow

功能：模版模式
网址：https://yq.aliyun.com/articles/71069?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13626

实例：股票查询客户端

"""

class StockQueryDevice():
    stock_code = "0"
    stock_price = 0.0
    def login(self, usr, pwd):
        pass
    def setCode(self, code):
        self.stock_code = code
    def queryPrice(self):
        pass
    def showPrice(self):
        pass

    def operateQuery(self, usr, pwd, code):
        if not self.login(usr, pwd):
            return False

        self.setCode(code)
        self.queryPrice()
        self.showPrice()
        return True

# WebA
class WebAStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockA" and pwd == "myPwdA":
            print("Web A: Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web A: Login ERROR...user:%s pwd:%s" % (usr, pwd))
            return False
    def queryPrice(self):
        print("Web A Querying...code:%s" % self.stock_code)
        self.stock_price = 20.00
    def showPrice(self):
        print("Web A Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))
# WebB
class WebBStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockB" and pwd == "myPwdB":
            print("Web B: Login OK...user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web B: Login ERROR...user:%s pwd:%s" % (usr, pwd))
            return False
    def queryPrice(self):
        print("Web B Querying...code:%s" % self.stock_code)
        self.stock_price = 30.00
    def showPrice(self):
        print("Web B Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


if __name__ == "__main__":
    web_a_query_dev = WebAStockQueryDevice()
    web_a_query_dev.operateQuery("myStockA", "myPwdA", "123456")