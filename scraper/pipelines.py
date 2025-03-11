import sqlite3
import json
from notonthehighstreet.items import ProductItem, ProductLinkItem, CategoryItem

class NotonthehighstreetPipeline:
    def open_spider(self, spider):
        if spider.name == 'product_spider':
            self.conn = sqlite3.connect('products_data.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS products_data (
                    product_url TEXT PRIMARY KEY,
                    Name TEXT,
                    Pre_discount_price TEXT,
                    Price TEXT,
                    Rating TEXT,
                    Number_of_comments TEXT,
                    Seller TEXT,
                    Number_of_photos INTEGER
                )
            ''')
        elif spider.name == 'product_links':
            self.conn = sqlite3.connect('products_links.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id TEXT,
                    product_url TEXT
                )
            ''')
        self.categories = []

    def close_spider(self, spider):
        if spider.name == 'categories':
            with open('categories_database.json', 'w', encoding='utf-8') as f:
                json.dump(self.categories, f, ensure_ascii=False, indent=4)
        self.conn.close()

    def process_item(self, item, spider):
        if spider.name == 'product_spider' and isinstance(item, ProductItem):
            self.cursor.execute('''
                INSERT OR REPLACE INTO products_data (
                    product_url, Name, Pre_discount_price, Price, Rating,
                    Number_of_comments, Seller, Number_of_photos
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.get('product_url'), item.get('Name'), item.get('Pre_discount_price'),
                item.get('Price'), item.get('Rating'), item.get('Number_of_comments'),
                item.get('Seller'), item.get('Number_of_photos')
            ))
            self.conn.commit()
        elif spider.name == 'product_links' and isinstance(item, ProductLinkItem):
            self.cursor.execute('''
                INSERT INTO products (product_id, product_url) VALUES (?, ?)
            ''', (item.get('product_id'), item.get('product_url')))
            self.conn.commit()
        elif spider.name == 'categories' and isinstance(item, CategoryItem):
            self.categories.append(item['category_url'])

        return item