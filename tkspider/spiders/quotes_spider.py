import scrapy
from scrapy.loader import ItemLoader
from ..items import AuthorItem, QuotesItems
from ..loaders import AuthorLoader, QuotesLoader
from . import BaseSpider
import random
from scrapy import Request


class QuotesSpider(BaseSpider):

    name = "quotes"  # уникальное паука имя для проекта

    def start_requests(self):
        self.total_count_ads = 0
        yield scrapy.Request('http://quotes.toscrape.com/page/1/', self.parse)

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # # вызывается поле успешной загрузки страниы
    # # Так же находит новые ссылки и создает новые scrapy.Request
    # def parse(self, response):
    #     # response = scrapy.http.TextResponse
    #     # https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.TextResponse
    #     # page = response.url.split('/')[-2]
    #     # filename = 'quotes-%s.html' % page
    #     # with open(filename, 'wb') as file:
    #     #     file.write(response.body)
    #     # self.log('saved file %s' % filename)
    #     print('\n\n\n\n############################################\n\n\n\n')
    #     # https://docs.scrapy.org/en/latest/intro/tutorial.html#extracting-data-in-our-spider
    #     for quote in response.css("div.quote"):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract()
    #         }
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page:
    #         # next_page = response.urljoin(next_page)
    #         # yield scrapy.Request(next_page, callback=self.parse)
    #         yield response.follow(next_page, callback=self.parse)

    #
    # вызывается поле успешной загрузки страниы
    def parse(self, response):
        import time
        # time.sleep(60)
        # l = QuotesLoader(item=QuotesItems(), response=response)
        # l.add_css('tags', 'div.tags a.tag::text')
        #
        # print(l.load_item())
        # exit(1)
        # вытаскиваем ссылки дальше по списку
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, self.parse)         # ВНИМАНИЕ: self.parse

        # вытаскиваем ссылки на страницы авторов
        for href in response.css('.author + a::attr(href)'):
            self.total_count_ads += 1
            yield response.follow(href, self.parse_author)  # ВНИМАНИЕ: self.parse_author
            yield response.follow('/udnefined_page_xdsedst', self.parse_author)
            yield Request(url='http://some-unavailabel-site.com/', callback=self.parse_author)

    # вытаскиваем данные по автору
    def parse_author(self, response):
        print(self.logger)
        # def extract_with_css(query):
        #     return response.css(query).extract_first().strip()
        #
        # yield {
        #     'name': extract_with_css('h3.author-title::text'),
        #     'birthdate': extract_with_css('.author-born-date::text'),
        #     'bio': extract_with_css('.author-description::text')
        # }
        l = AuthorLoader(item=AuthorItem(), response=response)
        l.add_css('name', 'h3.author-title::text')
        l.add_css('birth_date', '.author-born-date::text')
        # l.add_css('bio', '.author-description::text')
        result = l.load_item()
        self.logger.debug(result)

        if random.randint(1, 3) == 1:
            raise KeyError('crazy monkey error')
        return result
    # ВАЖНО: даная страница 'http://quotes.toscrape.com/page/1/'
    #       содержит цитаты
    #       и мы через цитаты вытаскивам авторов
    # проблема в том что 2х цитат могут вести ссылки на одного автора
    #
    # scrapy автоматически помнит посещеные страницы и не открывает их снова!
    # параметр DUPEFILTER_CLASS.
    #





