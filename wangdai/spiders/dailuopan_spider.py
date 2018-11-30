# -*- coding: utf-8 -*-

import scrapy

class Sprider(scrapy.Spider):
    name = "dailuopan"
    start_urls = [
        'http://www.dailuopan.com/pingji/all'

    ]

    def parse(self , response):
         for quote in response.css('td.t2'):
            yield {
                'text': quote.css('a::text').extract_first()
            }



