# -*- coding: utf-8 -*-
import scrapy
import crawler_type2.config as config
from crawler_type2.items import CrawlerType2Item


class TypeOne(scrapy.Spider):
    name = 'crawler_type1'

    def start_requests(self):
        source = getattr(self, 'source', None)
        if source is None or source not in config.SOURCES:
            print "No Source Found. Pass source"
            yield
        self.crawl_source = config.SOURCES[source]
        self.allowed_domains = self.crawl_source['ALLOWED_DOMAINS']
        self.start_urls = self.crawl_source['START_URLS']
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def parse(self, response):
        item = CrawlerType2Item()
        for element in response.xpath(self.crawl_source['XPATH']):
            text = element.xpath(self.crawl_source['TEXT_XPATH']).extract()
            item['text'] = " ".join(text)
            item['img'] = element.xpath(self.crawl_source['IMG_XPATH']).extract()

            yield item
