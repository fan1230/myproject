# -*- coding: utf-8 -*-
import scrapy
from review_anl.items import ReviewAnlItem
from scrapy.http import Request
import re,json


class AnlReviewSpider(scrapy.Spider):
    name = 'anl_review'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Myself-Belts-Toddler-Uniforms-White/product-reviews/B01HFEIBCM/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1']
    print('启动中...')

    def parse(self, response):
        item = ReviewAnlItem()
        color_f= response.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract()

        for i in range(len(color_f))[::2]:
            odd_num= color_f[i].split(sep=':')[1]
            item['color']=odd_num
            print(item['color'])

        for j in range(len(color_f))[1::2]:
            even_num=color_f[j].split(sep=':')[1]
            item['size'] = even_num
            print(item['size'])
        # item['size'] = response.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract()
        # item['customer'] = response.xpath('//a[@class="a-size-base a-link-normal author"]/text()').extract()
        # item['stars'] =re.compile('a-section celwidget">.*?title="(\d)out').findall(str(response.body))
        # print(item['color'])
        # print(item['size'])
        # print(item['customer'])
        # print(item['stars'])


        yield item

        # for i in range(2, 16):
        #     url = 'https://www.amazon.com/Myself-Belts-Toddler-Uniforms-White/product-reviews/B01HFEIBCM/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
        #     # 指定爬取网址和回调函数 实现自动爬取
        #
        #     yield Request(url, callback=self.parse)
