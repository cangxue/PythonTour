#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__(convert_charrefs=True)
        self.extract_data = []
        self.is_ul_active = None
        self.is_name_active = None
        self.is_time_active = None
        self.is_location_active = None

    def handle_starttag(self, tag, attrs):
        self.start_tag  = tag
        self.start_class = ''
        attrs = dict(attrs)
        if 'class' in attrs:
            self.start_class = attrs['class']
            if attrs['class'] == 'list-recent-events menu':
                self.is_ul_active = True
                self.extract_data.append([])
        if self.is_ul_active and tag == 'a':
            self.is_name_active = True
        if self.is_ul_active and tag == 'time':
            self.is_time_active = True
        if self.is_ul_active and self.start_class == 'event-location':
            self.is_location_active = True

    def handle_endtag(self, tag):
        if self.is_ul_active == True:
            if tag == 'ul':
                self.is_ul_active = False
            if tag == 'a':
                self.is_name_active = False
            if tag == 'time':
                self.is_time_active = False
            if tag == 'span' and self.start_class == 'event-location':
                self.is_location_active = False

    def handle_data(self, data):
        if self.is_ul_active == True:
            if self.start_tag == 'a' and self.is_name_active:
                self.extract_data[-1].append({'name': data})
            if self.start_tag == 'time' and self.is_time_active:
                self.extract_data[-1][-1]['time'] = data
            if self.start_class == 'event-location' and self.is_location_active:
                self.extract_data[-1][-1]['location'] = data

    def print_data(self):
        for i, value in enumerate(self.extract_data):
            if i == 0:
                print('Upcoming Events')
            else:
                print('You just missed...')
            for x in value:
                print('%20s %25s    %s' % (x['name'].encode('gbk', 'ignore').decode('gbk'), x['time'], x['location']))


def getHtml():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data

parser = MyHTMLParser()
html = getHtml()
parser.feed(html)
parser.print_data()