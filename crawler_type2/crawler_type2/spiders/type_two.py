# -*- coding: utf-8 -*-
import scrapy
import crawler_type2.config as config
from crawler_type2.items import CrawlerType2Item
import urlparse


class TypeTwo(scrapy.Spider):
    name = 'crawler_type2'

    def start_requests(self):
        source = getattr(self, 'source', None)
        if source is None or source not in config.SOURCES:
            raise Exception("Invalid source!!!")
        self.crawl_source = config.SOURCES[source]
        self.allowed_domains = self.crawl_source['ALLOWED_DOMAINS']
        self.start_urls = self.crawl_source['START_URLS']
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def parse(self, response):

        for href in response.xpath(self.crawl_source['LIST_PAGE_XPATH']):
            url = urlparse.urljoin(self.crawl_source['BASE_URL'], href.extract())
            print 'Sending request for url : ' + url
            req = scrapy.Request(url, callback=self.parse_item)
            # for key in response.meta.keys():
            #     req.meta[key] = response.meta[key]

            yield req

    def parse_item(self, response):
        print "parse item for url %s" % (response.request.url)
        item = CrawlerType2Item()
        for element in response.xpath(self.crawl_source['BLOG_CONTENT_XPATH']):
            heading = element.xpath(self.crawl_source['HEADING_XPATH']).extract()
            text = element.xpath(self.crawl_source['TEXT_XPATH']).extract()
            heading = [t.strip() for t in heading]
            text = [t.strip() for t in text]
            item['heading'] = " ".join(heading)
            item['text'] = " ".join(text)
            item['img'] = element.xpath(self.crawl_source['IMG_XPATH']).extract()

        if 'text' in item and len(item['text']) > 0:
            yield item
