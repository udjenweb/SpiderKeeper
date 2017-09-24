# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TkspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuotesItems(scrapy.Item):
    """"""
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    """"""
    name = scrapy.Field()
    birth_date = scrapy.Field()
    bio = scrapy.Field()


