# Imports

from pathlib import Path

import scrapy

# Class definition, our main spider for crawling
class BasicSpider(scrapy.Spider):
    # Spider name and default values for pages
    name = "Ryuzu"
    pages = 0

    # Start requests function
    def start_requests(self):
        # Get the URL argument from the command line
        url = getattr(self, 'url', None)  # Get the 'url' argument from command line
        # If the URL is not None, send a request to the URL
        if url:
            yield scrapy.Request(url=url, callback=self.parse)
        # Get the max_depth and max_pages arguments from the command line
        self.max_depth = int(getattr(self, 'max_depth', -1))
        self.max_pages = int(getattr(self, 'max_pages', -1))

    # Parse function
    def parse(self, response):
        # Finds the linked pages from the initial page
        secondary_pages = response.css("div.floatleft a::attr(href)").getall()
        # For each linked page, follow the link and call the parse_champ_page function
        for next_page in secondary_pages:
            # Check to make sure we should follow
            if (next_page is not None) and (self.max_depth == -1 or (response.meta["depth"] < self.max_depth)) and (self.max_pages == -1 or (self.pages < self.max_pages)):
                yield response.follow(next_page, callback=self.parse_champ_page, meta={"depth": response.meta["depth"] + 1})
                self.pages += 1

    # Parse function for the champion pages
    def parse_champ_page(self, response):
        # Get the page number
        page = response.url.split("/")[-2]
        # Create a folder for the HTML files
        folder_name = "../html_docs"
        Path(folder_name).mkdir(exist_ok=True)
        # Write the HTML file
        filename = Path(folder_name) / f"champion-{page}.html"
        Path(filename).write_bytes(response.body)
        # Follows linked pages. NOTE IN THE IMPLEMENTATION THIS IS USED IN, THIS DOES NOT ACCOMPLISH ANYTHING AS THE PAGES WOULD JUST LINK BACK TO THEMSELVES. THIS IS FOR MODULARITY
        secondary_pages = response.css("div.floatleft a::attr(href)").getall()
        for next_page in secondary_pages:
            if (next_page is not None) and (self.max_depth == -1 or (response.meta["depth"] < self.max_depth)) and (self.max_pages == -1 or (self.pages < self.max_pages)):
                yield response.follow(next_page, callback=self.parse)
                self.pages += 1