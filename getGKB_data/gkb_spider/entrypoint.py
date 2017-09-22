#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 11:09
# @Author  : huiliu@annoroad.com
# @Descript: 
# @File    : entrypoint.py
# @Software: PyCharm
from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'gkb_spider'])
