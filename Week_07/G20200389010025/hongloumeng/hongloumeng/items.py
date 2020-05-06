# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    star = scrapy.Field()
    vote = scrapy.Field()
    short = scrapy.Field()
    shorttime = scrapy.Field()
    new_star = scrapy.Field()
    sentiment = scrapy.Field()
