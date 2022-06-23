# -*- coding: utf-8 -*-
import scrapy


class DemoScrapeSpiderXPath(scrapy.Spider):
    name = 'demo-xpath'
    start_urls = [
        'https://www.dexciss.com/?page_id=213',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="et_pb_text_inner"]'):
            yield {
                # 'brochure': quote.xpath('.//h1/text()').extract(),
                # 'details': quote.xpath('.//p/text()').extract(),
                'brochures': quote.xpath('.//h1/text()').extract(),
                'details': quote.xpath('.//div[@class="et_pb_text_inner"]/p/text()').extract(),
            }

        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

