import json
import scrapy
import re

base_url = 'https://gearvn.com'


class ProductSpider(scrapy.Spider):
    name = 'product'
    link = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('./data/category/data_category.json', 'r') as json_file:
            content_file = json.load(json_file)
            all_link = []
            for category in content_file:
                all_link.append(category["link_category"])

            self.start_urls = all_link
        json_file.close()

    def parse(self, response):
        data_link_page_product = {}
        all_link_page = []
        total_page = 0
        all_li_pagination = response.css('ul.pagination-list li.hidden-phone')
        for itemPagination in all_li_pagination:
            link_product = itemPagination.css(
                'a.pagenav::attr(href)').extract_first()
            all_link_page.append(link_product)

        if len(all_link_page) > 0:
            last_page = all_link_page[-1]
            total_page = int(re.search(r'\d+', last_page).group(0))

        if total_page > 0:
            for i in range(total_page):
                link_page_product = str(response.request.url) + "?page=" + str(i + 1)
                self.link.append(link_page_product)
        else:
            self.link.append(response.request.url)

        with open('./data/product/page/page.json', 'w') as content_json:
            json.dump(self.link, content_json)
        yield data_link_page_product
