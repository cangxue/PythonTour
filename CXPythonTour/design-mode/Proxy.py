# coding=utf-8

"""
Created on 2017-11-15
@author: Palesnow

功能：代理模式
网址：https://yq.aliyun.com/articles/70738?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11965

实例：网络服务器配置白名单
"""

# 该服务器接受如下格式数据，addr代表地址，content代表接受的信息内容
# info_struct = dict()
# info_struct["addr"] = 10000
# info_struct["content"] = "hahah"

# ====抽象对象角色====
# 抽象主题类
class Server:
    content = ""
    def recv(self, info):
        pass
    def show(self):
        pass
# ====目标对象角色====
# 具体主题类
class infoServer(Server):
    def recv(self, info):
        self.content = info
        return "recv OK!"
    def show(self):
        print("SHOW: %s" % self.content)


# ====代理对象角色====
# 抽象代理
class serverProxy:
    pass

# Server的直接接口代理
class infoServerProxy(serverProxy):
    server = ""  # 控制代理的服务器对象
    def __init__(self, server):
        self.server = server
    def recv(self, info):
        return self.server.recv(info)
    def show(self):
        self.server.show()

# Server白名单的直接接口代理
class whiteInfoServerProxy(infoServerProxy):
    white_list = [10000, 10001]
    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info structure is not correct"

        addr = info.get("addr", 0)
        if not addr in self.white_list:
            return "Your address is not in the white list."
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def addWhite(self, addr):
        self.white_list.append(addr)
    def rmvWhite(self, addr):
        self.white_list.remove(addr)
    def clearWhite(self):
        self.white_list = []


if __name__ == "__main__":
    # 接受的内容
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"

    # 初始化服务器
    info_server = infoServer()

    # infoServerProxy
    print("========infoServerProxy==========")
    info_server_proxy = infoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()

    # whiteInfoServerProxy
    print("========whiteInfoServerProxy==========")
    white_info_server_proxy = whiteInfoServerProxy(info_server)
    print(white_info_server_proxy.recv(info_struct))
    white_info_server_proxy.show()

    print("=======添加白名单数据===========")
    white_info_server_proxy.addWhite(10010)
    print(white_info_server_proxy.recv(info_struct))
    white_info_server_proxy.show()


