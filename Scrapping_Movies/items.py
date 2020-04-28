  # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrappingMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    actor_name = scrapy.Field()
    actor_info = scrapy.Field()
    actor_movie = scrapy.Field()
    actor_imageLink = scrapy.Field()

