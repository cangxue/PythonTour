#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-14
@author: Palesnow

@content: 糗事百科爬取
@参考资料：http://wiki.jikexueyuan.com/project/python-crawler-guide/jokes.html

"""

import requests
from bs4 import BeautifulSoup

# 爬虫类
class QSBK:
    # 初始化方法，定义变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子
        self.stores = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            # 设置URL
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 获取页面代码
            response = requests.get(url, headers=self.headers)

            return response.text
        except requests.RequestException as e:
            print(e)

    # 传入某一页的索引，返回本页不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败。。。')
            return None
        # 处理数据
        pageStores = []
        soup = BeautifulSoup(pageCode, 'html.parser')
        for tag in soup.find_all(class_='article block untagged mb15 typs_hot'):
            if not tag.find_all(class_='thumb'):
                user_name = tag.findAll(r'h2')[0].text.strip()
                user_content = tag.find_all(class_='content')[0].text.strip()
                tag1 = tag.find_all(class_='stats-vote')[0]
                stats_vote = tag1.find_all(class_='number')[0].text.strip()
                temp = [user_name, user_content, stats_vote]
                pageStores.append(temp)

        return pageStores

    # 加载并提取页面内容，加入列表中
    def loadPage(self):
        if self.enable == True:
            pageStores = self.getPageItems(self.pageIndex)
            if pageStores:
                self.stores.append(pageStores)

    # 数据加载判断
    def getOneStory(self, pageStores, page):
        for story in pageStores:
            print("第%d页\t发布人:%s\n%s\n赞:%s\n" % (page, story[0], story[1], story[2]))

        inputs = input("点击S开始，点击Q结束:")
        if inputs == "S":
            self.pageIndex += 1
            self.loadPage()
        elif inputs == 'Q':
            self.enable = False
            return
    # 开始方法
    def start(self):
        print('正在读取糗事百科,按S查看新段子，Q退出')
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        while self.enable:
            if len(self.stores) > 0:
                # 从全局list中获取一页的段子
                pageStores = self.stores[0]
                # 当前读到的页数加一
                # 将全局list中第一个元素删除，因为已经取出
                del self.stores[0]
                # 输出该页的段子
                self.getOneStory(pageStores, self.pageIndex)

spider = QSBK()
spider.start()



