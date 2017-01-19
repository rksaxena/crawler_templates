# -*- coding: utf-8 -*-
import scrapy
import crawler_type1.config as config
import crawler_type1.utils as utils
from crawler_type1.items import CrawlerType1Item


class TypeOne(scrapy.Spider):
    name = 'crawler_type1'

    def start_requests(self):
        source = getattr(self, 'source', None)
        if source is None or source not in config.SOURCES:
            raise Exception("Invalid source!!!")
        self.crawl_source = config.SOURCES[source]
        self.allowed_domains = self.crawl_source['ALLOWED_DOMAINS']
        self.start_urls = self.crawl_source['START_URLS']
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def parse(self, response):
        item = CrawlerType1Item()
        for element in response.xpath(self.crawl_source['XPATH']):
            text = element.xpath(self.crawl_source['TEXT_XPATH']).extract()
            heading = ""
            if 'HEADING_XPATH' in self.crawl_source:
                heading = element.xpath(self.crawl_source['HEADING_XPATH']).extract()
                heading = [t.strip() for t in heading]
            item['heading'] = " ".join(heading)
            item['text'] = utils.extract_text(" ".join(text))
            item['img'] = element.xpath(self.crawl_source['IMG_XPATH']).extract()

            yield item
