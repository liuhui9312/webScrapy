# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GkbSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pa_id = scrapy.Field()
    genes = scrapy.Field()
    chemicals = scrapy.Field()
    pvalue = scrapy.Field()
    literature = scrapy.Field()
    significance = scrapy.Field()
    phenotypeCategories = scrapy.Field()
    variants = scrapy.Field()
    cases = scrapy.Field()
    characteristics = scrapy.Field()
    race = scrapy.Field()
    sentence = scrapy.Field()
    literatureUrl = scrapy.Field()
    id = scrapy.Field()
    num = scrapy.Field()
    notes = scrapy.Field()

