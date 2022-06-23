# -*- coding: utf-8 -*-
import scrapy


class DemoScrapeCSSSpider(scrapy.Spider):
    name = "demo-css"
    start_urls = [
        'https://www.dexciss.com/?page_id=213',
    ]

    def parse(self, response):
        for quote in response.css("div.et_pb_text_inner"):
            yield {
                'heading': quote.css("h1::text"),
                # 'description': quote.css("span::text").extract_first(),
                'paragraph': quote.css("p::text")
            }

        # next_page_url = response.css("li.next > img::attr(src)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

