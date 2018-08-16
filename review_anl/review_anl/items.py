# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewAnlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    color=scrapy.Field()
    size=scrapy.Field()
    stars=scrapy.Field()
    customer=scrapy.Field()


