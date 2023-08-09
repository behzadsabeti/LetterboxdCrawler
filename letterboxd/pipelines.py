import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LetterboxdPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        length = adapter.get("length")
        length = re.findall(r'\d+', length)[0]
        adapter["length"] = length

        ids = ["imdb_id", "tmdb_id"]
        for val in ids:
            value = adapter.get(val)
            value = value.split("/")[4]
            adapter[val] = value

        ratings = adapter.get("histogram")
        ratings = [int(rate.split("\xa0")[0].replace(",","")) for rate in ratings]
        adapter["histogram"] = ratings

        return item
