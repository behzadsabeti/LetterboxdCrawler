import scrapy
from letterboxd.items import MovieItem

class MoviedetailSpider(scrapy.Spider):
    name = "MovieDetail"
    allowed_domains = ["letterboxd.com"]
    
    def start_requests(self):
        base_url = "https://letterboxd.com/films/ajax/popular/page/"
        num_pages = 100

        for page_number in range(1, num_pages + 1):
            url = f"{base_url}{page_number}/"
            yield scrapy.Request(url, callback=self.parse_page)


    def parse_page(self, response):
        items = response.css("ul.poster-list li div")
        for item in items:
            movie_name = item.attrib["data-target-link"]
            movie_url = "https://letterboxd.com" + movie_name
            yield scrapy.Request(movie_url, callback=self.extract_movie_details, meta={"movie_name": movie_name})


    def extract_movie_details(self, response):
        movieitem = MovieItem()
        movieitem["name"] = response.css("section#featured-film-header h1.headline-1::text").get()
        movieitem["year"] = response.css("section#featured-film-header p small.number a::text").get()
        movieitem["director"] = response.css("section#featured-film-header p a span.prettify::text").get()
        movieitem["length"] = response.css("p.text-link::text").get()
        movieitem["genres"] = response.css("#tab-genres > div:nth-child(2) > p a::text").getall()
        movieitem["themes"] = response.css("#tab-genres > div:nth-child(4) > p > a::text").getall()[:-1]
        movieitem["imdb_id"] = response.css("#film-page-wrapper > div.col-17 > section.section.col-10.col-main > p > a:nth-child(1)").attrib["href"]
        movieitem["tmdb_id"] = response.css("#film-page-wrapper > div.col-17 > section.section.col-10.col-main > p > a:nth-child(2)").attrib["href"]

        movie_name = response.meta['movie_name'].split("/")[2]
        histogram_url  = "https://letterboxd.com/csi/film/{}/rating-histogram/".format(movie_name)
        yield scrapy.Request(histogram_url, callback=self.histogram_parse, meta={'movieitem': movieitem})



    def histogram_parse(self, response):
        movieitem = response.meta['movieitem']
        ratings = response.css("ul li.rating-histogram-bar a::text").getall()
        movieitem["histogram"] = ratings
        yield movieitem
