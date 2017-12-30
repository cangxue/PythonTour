#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-28
@author: Palesnow

@content: 豆瓣爬取
          1、获取排行榜
          2、获取影评

"""

import requests
import re
import json


class DOUBAN:
    # 初始化
    def __init__(self, baseUrl):
        self.baseURL = baseUrl

    def getPage(self, pageNum):
        try:
            url = self.baseURL + 'start=' + str(pageNum) + '&type=T'
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return None
        except requests.RequestException as e:
            print(e)
    def getContent(self, page):
        pattern = re.compile('<table width=".*?<div class="pl2">.*?>(.*?)</a>.*?class="pl">(.*?)</p>'
                             + '.*?<span class="rating_nums">(.*?)</span>.*?class="pl">(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            yield {
                'title': item[0].split("/")[0].strip(),
                'actor': item[1].split("/"),
                'average': item[2],
                'content': item[3],
            }
    def start(self):
        for i in range(0, 2):
            page = self.getPage(i)
            print("===============================第%s数据======================" % i)
            for item in self.getContent(page):
                print(item)



url = 'https://movie.douban.com/tag/2016?'
douban = DOUBAN(url)
douban.start()







