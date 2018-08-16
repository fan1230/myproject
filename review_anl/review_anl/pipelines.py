# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class ReviewAnlPipeline(object):
    def __init__(self):
        self.file = codecs.open(r"E:\工作文件\anl_reviews.txt", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        # 循环遍历商品信息
        # for j in range(0, len(item['color'])):
        #     for i in range(0,j):
        #         color = item['color'][i][0]
        #         size = item['color'][i][1]
        #     # customer = item['customer'][j]
        #     # stars = item['stars'][j]
        #     # 重新组合成字典
        #         goods = {'color': color, 'size': size}
        #
        #         aa = json.dumps(dict(goods), ensure_ascii=False)
        #         line = aa + '\n'
        aa=json.dumps((item['color']), ensure_ascii=False)
        line = aa + '\n'
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

    print('运行完成!')

