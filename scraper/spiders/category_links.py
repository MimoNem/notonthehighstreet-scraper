import scrapy
from notonthehighstreet.items import CategoryItem

class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['notonthehighstreet.com']
    start_urls = ['https://www.notonthehighstreet.com/']

    def parse(self, response):
        links = response.css('ul.DepartmentsNav___StyledUl-sc-1n4vtmh-0.fUPvhZ a::attr(href)').getall()
        full_links = [response.urljoin(link) for link in links]
        filtered_links = [link for link in full_links if link.count('/') >= 5]
        excluded_links = response.xpath('//*[@id=\"__next\"]/div[4]/nav/ul/li[11]//a/@href').getall()
        excluded_full_links = [response.urljoin(link) for link in excluded_links]
        filtered_links = [link for link in filtered_links if link not in excluded_full_links]

        for link in filtered_links:
            yield CategoryItem(category_url=link)


            