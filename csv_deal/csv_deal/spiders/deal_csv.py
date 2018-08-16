# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from csv_deal.items import CsvDealItem
import re,urllib.request
import csv

class DealCsvSpider(scrapy.Spider):
    name = 'deal_csv'
    allowed_domains = ['amazon.com']
    # csv_i='belt'
    # #
    # def start_requests(self):
    #     yield Request('https://www.amazon.com/s/&field-keywords='+str(self.csv_i),
    #                   headers=None
    #                   )

    print('初始化...')
    print('打开csv中...')
    csv_file = open(r'E:\工作文件\new csv.csv')
    data = list(csv.reader(csv_file))
    # start_urls = ['https://www.amazon.com/s/&field-keywords=' + str(data[0][0])]
    def start_requests(self):
        yield Request('https://www.amazon.com/s/&field-keywords='+str(self.data[1][0]),
                      headers={
                          'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                      }
                      )


    def parse(self, response):
        item=CsvDealItem()
        try:
            item['result']=re.compile('s-result-count.*?over(.*?)results for.*?"a-color-state a-text-bold"').findall(str(response.body))[0]
            print(item['result'])
        except:
            print('miss')
        #
        for i in range(3,len(self.data)+1):
            nexturl='https://www.amazon.com/s/&field-keywords=' + str(self.data[i][0])
            # print(nexturl)
        # yield Request(nexturl,callback=self.parse)
            yield Request(nexturl,callback=None,headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            })
