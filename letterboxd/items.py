# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    
    name = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    length = scrapy.Field()
    genres = scrapy.Field()
    themes = scrapy.Field()
    imdb_id = scrapy.Field()
    tmdb_id = scrapy.Field()
    histogram = scrapy.Field()