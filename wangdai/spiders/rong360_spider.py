# -*- coding: utf-8 -*-

import scrapy

class Sprider(scrapy.Spider):
    name = "r360"
    start_urls = [
        'https://www.rong360.com/licai-p2p/pingtai/rating'

    ]


    def parse(self , response):
         for quote in response.css('div.tab-all'):
             yield {
                 'name': quote.css('td.pt_name a::text').extract(),
                 'pingji': quote.css('td.pingji::text').extract_first().replace(" ", "").replace("\r\n", "").replace(
                     "\u00a0", ""),
             }




