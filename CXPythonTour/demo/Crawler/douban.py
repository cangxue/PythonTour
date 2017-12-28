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

    def getPage:
        try:
            response = requests.get(set.baseURL)





