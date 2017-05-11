# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyntraItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_details = scrapy.Field()
    product_image_location = scrapy.Field()
