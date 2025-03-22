from bs4 import BeautifulSoup
import cloudscraper
import json

from .base_parser import ParserBase


BASE_URL = "https://www.atbmarket.com"
url = "https://www.atbmarket.com/catalog/388-aktsiya-7-dniv"
API_URL = 'http://127.0.0.1:8000/products/'


class ATBParser(ParserBase):    
    def get_html(self):
        scraper = cloudscraper.create_scraper()
        html = scraper.get(self.store_url).text

        with open("server/parse_data/htmls/atb.html", "w", encoding="utf-8") as file:
            file.write(html)
        

    def set_src(self):
        with open(f'parse_data/htmls/atb.html', encoding='utf-8') as file:
            src = file.read()
        self.src = src


    def get_products(self):
        soup = BeautifulSoup(self.src, 'lxml')
        product_list = list(soup.find_all('article', class_='catalog-item js-product-container'))
        print(type(product_list))
        return product_list


    def get_data(self, product):
        title_block = product.find('div', class_='catalog-item__info').find('div', class_='catalog-item__title')
        name = title_block.find('a').text
        url_in_store = f"{BASE_URL}{title_block.find('a').get('href')}"
        
        price_block = product.find('div', class_='catalog-item__bottom').find('div', class_="catalog-item__product-price")
        old_price = price_block.find('data', class_='product-price__top').get('value')
        new_price = price_block.find('data', class_='product-price__bottom').get('value')
        
        discount_text = product.find('div', class_='catalog-item__photo').find('div', class_='catalog-item__labels').find('span').text
        discount = discount_text.strip().replace('%', '').replace('\n', '').strip()

        data = {
            "name": str(name),
            "description": "qwerty",
            "old_price": float(old_price),
            "new_price": float(new_price),
            "discount_percent": int(discount),
            "url_in_store": url_in_store,
            "store_id": 2,
            "category_id": 1,
            "start_date": "09-03-2025",
            "end_date": "16-03-2025"
        }
        print(data)
        return data
    
