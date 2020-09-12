# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EarthquakeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    location = scrapy.Field()
    earthquake_time = scrapy.Field()
    strength = scrapy.Field()

