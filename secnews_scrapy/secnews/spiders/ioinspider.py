# -*- coding: utf-8 -*-
import scrapy
from secnews.items import SecnewsItem

class IoinspiderSpider(scrapy.Spider):
    name = 'ioinspider'
    allowed_domains = ['wiki.ioin.in']
    start_urls = ['http://wiki.ioin.in/']
    def parse(self, response):
        item = SecnewsItem()
        table=response.xpath('/html/body/div[1]/table/tbody/tr')
        for each in table:
            item['time']=each.css('tr td::text').extract_first()
            item['title']=each.css('tr td a.visit-color::text').extract_first()
            item['title']=item['title'].replace(' ','').replace('\n','')
            item['category']=each.css('tr td a.color-000::text').extract_first()
            item['clickANDcomment']=each.css('td.text-center a.color-000::text').extract_first()
            yield item

