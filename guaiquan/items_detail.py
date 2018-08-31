# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaiquanDetailItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    head_img_url = scrapy.Field()
    pass

    def get_classname(self):
        return self.__class__.__name__
