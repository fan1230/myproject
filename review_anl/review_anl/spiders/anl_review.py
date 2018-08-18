# -*- coding: utf-8 -*-
'''
此函数可用于爬取anazom上单个listing的信息
'''
import scrapy
from review_anl.items import ReviewAnlItem
from scrapy.http import Request
import re,json


class AnlReviewSpider(scrapy.Spider):
    name = 'anl_review'
    allowed_domains = ['amazon.com']
    #输入需要抓取的网址
    # start_urls = ['https://www.amazon.com/Elastic-Adjustable-Strech-Silver-Square/product-reviews/B00AKCCB0U/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def start_requests(self):


        yield Request('https://www.amazon.com/Running-Runtasty-Samsung-Waterproof-Sleekest/product-reviews/B01G7JOQSO/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1',
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
                      }
                      )

    print('启动中...')

    def parse(self, response):
        item = ReviewAnlItem()
        item['color']= response.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract()

        # item['color']={}
        # for i in range(len(color_f))[::2]:
        #     odd_num= color_f[i].split(sep=':')[1]
        #     print(odd_num)
        #     print(type(odd_num))
        #     item['color'].append(odd_num)
        #     # print(item['color'])
        #
        # for j in range(len(color_f))[1::2]:
        #     even_num=color_f[j].split(sep=':')[1]
        #     item['size'] = even_num
            # print(item['size'])
        # item['size'] = response.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract()
        # item['customer'] = response.xpath('//a[@class="a-size-base a-link-normal author"]/text()').extract()
        # item['stars'] =re.compile('a-section celwidget">.*?title="(\d)out').findall(str(response.body))
        # print(item['color'])
        # print(item['size'])
        # print(item['customer'])
        # print(item['stars'])

        yield item

        # last_page=int(response.xpath('//li[@class="a-last"]/preceding-sibling::li[1]/a/text()').extract()[0])

        # for i in range(2, last_page):
        for i in range(2, 9):
            url = 'https://www.amazon.com/Running-Runtasty-Samsung-Waterproof-Sleekest/product-reviews/B01G7JOQSO/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
            # 指定爬取网址和回调函数 实现自动爬取
            yield Request(url, callback=self.parse,headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
                      })
