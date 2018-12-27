# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SecnewsItem(scrapy.Item):

    time = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    clickANDcomment = scrapy.Field()
    pass
