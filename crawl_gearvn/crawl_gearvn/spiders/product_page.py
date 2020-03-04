import json
import scrapy

base_url = 'https://gearvn.com'


class ProductPageSpider(scrapy.Spider):
    name = 'productpage'
    link = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('./data/product/page/page.json', 'r') as json_file:
            content_file = json.load(json_file)
            all_link = []
            for page in content_file:
                print(page)
                all_link.append(page)

            self.start_urls = all_link
        json_file.close()

    def parse(self, response):
        div_product_row_img = response.css('div.product-row-img')
        for item in div_product_row_img:
            text_product_detail = item.css('a::attr(href)').get()
            link_product_detail = '{}{}'
            link_full = link_product_detail.format(
                self.base_url, text_product_detail)
            print(link_full)
            # print('/n')
            # self.link.append(link_full)

        # with open('./data/product/product_link.json', 'w') as content_json:
        #     json.dump(self.link, content_json)
