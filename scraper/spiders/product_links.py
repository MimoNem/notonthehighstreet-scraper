import json
import scrapy
import math
from notonthehighstreet.items import ProductLinkItem

class ProductLinksSpider(scrapy.Spider):
    name = 'product_links'

    def __init__(self):
        super(ProductLinksSpider, self).__init__()
        with open('categories_database.json', 'r', encoding='utf-8') as f:
            self.urls = json.load(f)

        self.current_url_index = 0
        self.current_page = 1
        self.total_pages = 1

    def start_requests(self):
        if self.current_url_index < len(self.urls):
            url = self.urls[self.current_url_index]
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_count_element = response.css('p.sc-f22be243-8.mIoyC::text').re_first(r'\d+')

        if product_count_element:
            product_count = int(product_count_element)
            self.total_pages = math.ceil(product_count / 60)
            self.current_page = 1

            paginated_url = f"{response.url}?page={self.current_page}"
            yield scrapy.Request(url=paginated_url, callback=self.parse_page)

    def parse_page(self, response):
        product_cards = response.css('[data-testid="PRODUCT_CARD_GRID_ITEM_TEST_ID"]')

        for card in product_cards:
            product_id = card.attrib.get('data-productid')
            href = card.css('a::attr(href)').get()

            if product_id and href:
                if href.startswith('/'):
                    href = response.urljoin(href)
                item = ProductLinkItem(product_id=product_id, product_url=href)
                yield item

        self.current_page += 1
        if self.current_page <= self.total_pages:
            next_page_url = f"{response.url.split('?')[0]}?page={self.current_page}"
            yield scrapy.Request(url=next_page_url, callback=self.parse_page)
        else:
            self.current_url_index += 1
            if self.current_url_index < len(self.urls):
                next_url = self.urls[self.current_url_index]
                yield scrapy.Request(url=next_url, callback=self.parse)