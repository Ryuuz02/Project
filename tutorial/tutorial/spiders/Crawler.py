from pathlib import Path

import scrapy


class BasicSpider(scrapy.Spider):
    name = "Ryuzu"
    pages = 0

    def start_requests(self):
        url = getattr(self, 'url', None)  # Get the 'url' argument from command line
        if url:
            yield scrapy.Request(url=url, callback=self.parse)
        self.max_depth = int(getattr(self, 'max_depth', -1))
        self.max_pages = int(getattr(self, 'max_pages', -1))

    def parse(self, response):
        secondary_pages = response.css("div.floatleft a::attr(href)").getall()
        for next_page in secondary_pages:
            if (next_page is not None) and (self.max_depth == -1 or (response.meta["depth"] < self.max_depth)) and (self.max_pages == -1 or (self.pages < self.max_pages)):
                yield response.follow(next_page, callback=self.parse_champ_page, meta={"depth": response.meta["depth"] + 1})
                self.pages += 1
    def parse_champ_page(self, response):
        page = response.url.split("/")[-2]
        folder_name = "../html_docs"
        Path(folder_name).mkdir(exist_ok=True)
        filename = Path(folder_name) / f"champion-{page}.html"
        information = response.css("main.page__main").get()
        Path(filename).write_bytes(response.body)
        secondary_pages = response.css("div.floatleft a::attr(href)").getall()
        for next_page in secondary_pages:
            if (next_page is not None) and (self.max_depth == -1 or (response.meta["depth"] < self.max_depth)) and (self.max_pages == -1 or (self.pages < self.max_pages)):
                yield response.follow(next_page, callback=self.parse)
                self.pages += 1