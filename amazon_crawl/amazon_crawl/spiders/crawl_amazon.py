# -*- coding: utf-8 -*-
import scrapy


class CrawlAmazonSpider(scrapy.Spider):
    name = 'crawl_amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
