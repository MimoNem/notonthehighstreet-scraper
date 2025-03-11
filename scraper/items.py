import scrapy

class ProductItem(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    Name = scrapy.Field()
    Pre_discount_price = scrapy.Field()
    Price = scrapy.Field()
    Rating = scrapy.Field()
    Number_of_comments = scrapy.Field()
    Seller = scrapy.Field()
    Number_of_photos = scrapy.Field()

class ProductLinkItem(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()

class CategoryItem(scrapy.Item):
    category_url = scrapy.Field()