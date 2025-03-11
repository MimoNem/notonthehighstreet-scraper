import scrapy
import sqlite3
import time
from notonthehighstreet.items import ProductItem

class ProductSpider(scrapy.Spider):
    name = 'product_spider'

    def start_requests(self):
        conn = sqlite3.connect('products_links.db')
        cursor = conn.cursor()
        cursor.execute("SELECT product_ID, product_URL FROM products")
        self.rows = cursor.fetchall()
        conn.close()

        if self.rows:
            product_id, product_url = self.rows.pop(0)
            yield scrapy.Request(url=product_url, callback=self.parse, meta={'product_id': product_id})

    def parse(self, response):
        product_id = response.meta['product_id']

        sc_48b8a1d4_2_dYFvoZ_count = len(response.css('.sc-48b8a1d4-2.dYFvoZ'))
        if sc_48b8a1d4_2_dYFvoZ_count == 0:
            sc_48b8a1d4_2_dYFvoZ_count = 1

        item = ProductItem(
            product_id=product_id,
            product_url=response.url,
            Name=response.xpath('//*[@id="__next"]/main/div[2]/div[2]/h1/text()').get(default=''),
            Pre_discount_price=response.xpath(
                '//*[@id="__next"]/main/div[2]/div[3]/div/div/p[2]/text()').re_first(r'£([\d.]+)', default=''),
            Price=response.xpath(
                '//*[@id="__next"]/main/div[2]/div[2]/div[3]/div[1]/div/p/text()').re_first(r'£([\d.]+)', default=''),
            Rating=response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[4]/a/span[1]/text()').get(default=''),
            Number_of_comments=response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[4]/a/span[3]/text()').re_first(r'\d+', default=''),
            Seller=response.xpath('//*[@id="partner-module-id"]/div/div[1]/div/div[1]/h2/a/@href').re_first(r'/([^/]+)$', default=''),
            Number_of_photos=sc_48b8a1d4_2_dYFvoZ_count
        )

        yield item

        if self.rows:
            product_id, product_url = self.rows.pop(0)
            time.sleep(9)  # Delay between requests
            yield scrapy.Request(url=product_url, callback=self.parse, meta={'product_id': product_id})