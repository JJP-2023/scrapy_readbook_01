# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyReadbook01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 图片
    src = scrapy.Field()

    href = scrapy.Field()

    price = scrapy.Field()

    author = scrapy.Field()

    publisher = scrapy.Field()

