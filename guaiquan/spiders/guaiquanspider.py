import scrapy
import io
import sys
from guaiquan.items import GuaiquanItem
from guaiquan.items_detail import GuaiquanDetailItem

class IconSpider(scrapy.Spider):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    name = "guaiquanspider"
    allowed_domains = ["18183.com"]
    start_urls = [
        "http://www.18183.com/yxzjol/?soucre=bdald"
    ]
    detail_urls = []

    def parse(self, response):
        items = response.xpath('//div[@class="article-list"]/div[@class="tab-list clearfix"]/div[@class="tab-item clearfix on"]/ul/li/a')
        for i in items:
            # print (i.xpath('./@href').extract()[0])
            # print (i.xpath('./@title').extract()[0])
            item = GuaiquanItem()
            item["title"] = i.xpath('./@title').extract()[0]
            item["url"] = i.xpath('./@href').extract()[0]
            self.detail_urls.append(item["url"])
            yield item

        for j in self.detail_urls:
            yield scrapy.Request(j, callback=self.parseHeaderImageUrl)


    def parseHeaderImageUrl(self, response):
        # print ('-------')
        # print (response.url)
        items = response.xpath('//div[@class="arc-body"]//img')
        head_img_url = items[0].xpath('./@src').extract()[0]
        item = GuaiquanDetailItem()
        item["url"] = response.url
        item["head_img_url"] = head_img_url
        # print (head_img_url)
        yield item
