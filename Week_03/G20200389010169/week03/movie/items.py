# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    ranking = scrapy.Field()
    cover = scrapy.Field()
    #views = scrapy.Field()
