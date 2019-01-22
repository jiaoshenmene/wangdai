# -*- coding: utf-8 -*-

import scrapy

class Sprider(scrapy.Spider):
    name = "zj"
    start_urls = [
        'https://www.wdzj.com/pingji.html'

    ]


    def parse(self , response):
         for quote in response.css('div.tb-platname'):
             yield {
                 'name': quote.css('a::text').extract_first(),

             }