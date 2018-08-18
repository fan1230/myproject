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
    reader=csv.reader(csv_file)
    column = [row[0] for row in reader]
    # start_urls = ['https://www.amazon.com/s/&field-keywords=' + str(data[0][0])]
    # print(data)
    def start_requests(self):
        print(self.column[5])

        yield Request('https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3\
        Daps&field-keywords='+str(self.column[5]),
                      headers={
                          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
                      }
                      )


    def parse(self, response):
        item=CsvDealItem()
        try:
            dis_num=re.compile('s-result-count.*?over(.*?)results for.*?"a-color-state a-text-bold"').findall(str(response.body))[0]
            if dis_num.isdigit():
                item['result']=dis_num
            else:
                dis_num = re.compile('s-result-count.*?of(.*?)results for.*?"a-color-state a-text-bold"').findall(str(response.body))[0]
                item['result'] = dis_num
            print(item['result'])
        except:
            print('miss')
        #
        # for i in range(3,len(self.data)+1):
        #     nexturl='https://www.amazon.com/s/&field-keywords=' + str(self.data[i][0])
        #     # print(nexturl)
        # # yield Request(nexturl,callback=self.parse)
        #     yield Request(nexturl,callback=None,headers={
        #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        #     })
