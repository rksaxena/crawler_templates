# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CrawlerType2Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    heading = Field()
    text = Field()
    img = Field()
