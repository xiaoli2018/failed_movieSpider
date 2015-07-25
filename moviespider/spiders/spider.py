# -*- coding:utf-8 -*-
__author__ = 'heng'
import sys
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader, Identity
from moviespider.items import MoviespiderItem
import re
import urllib

class Moviespider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ['dytt8.net']
    start_urls = [
        "http://www.dytt8.net/",
    ]

    def parse(self, response):
        sel = Selector(response)
        items = []
        item = MoviespiderItem()
        for link in sel.xpath('//div[@class="co_content2"]/ul/a/@href').extract():
            link = 'http://www.dytt8.net' + link
            pageresponse = urllib.urlopen(link).read().decode('gbk')
            item['name'] = re.findall('<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>',pageresponse,re.S)
            item['link'] = re.findall('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">',pageresponse,re.S)
            items.append(item)
            yield items

            # PageResponse = scrapy.Request(link,callback=)
            # print PageResponse
            # pagesel = Selector(PageResponse)
            # item['name'] = pagesel.xpath('//div[@class="title_all"]/h1/font/@color').extract()
            # item['link'] = pagesel.xpath('//tr/td[@style="WORD-WRAP"]/a/@href').extract()
            # items.append(item)



            # l = ItemLoader(item = MoviespiderItem(),response=response)
            # item = MoviespiderItem()
            # item['link'] = scrapy.Request(link,callback = l.add_xpath('link','//tr/td[@style="WORD-WRAP"]/a/@href'))
            #yield item

    def parse_items(self,response):
        l = ItemLoader(item = MoviespiderItem(),response=response)
        #l.add_xpath('name','//div[@class="title_all"]/h1/font/@color')
        l.add_xpath('link','//tr/td[@style="WORD-WRAP"]/a/@href',Identity())
    #
    #
    #     return l.load_item()
            


