import json

import scrapy
import re

base_url = 'https://gearvn.com'


class ProductSpider(scrapy.Spider):
    name = 'product'

    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('./data/category/data_category.json') as json_file:
            content_file = json.load(json_file)
            for category in content_file:
                self.start_urls.append(category["link_category"])

    def parse(self, response):
        all_li_pagination = response.css('ul.pagination-list li.hidden-phone')
        all_link_page = []
        for itemPagination in all_li_pagination:
            link_product = itemPagination.css('a.pagenav::attr(href)').extract_first()
            all_link_page.append(link_product)

        last_page = all_link_page[-1]
        total_page = int(re.search(r'\d+', last_page).group(0))
        for i in range(total_page):
            link_page_producr = "https://gearvn.com/collections/laptop?page=" + str(i + 1)
            data_link_page_producr = {
                'link_page_producr': link_page_producr,
            }
            yield data_link_page_producr

        # with open('./data/category/data_category.json') as json_file:
        #     content_file = json.load(json_file)
        #     for category in content_file:
        #         yield response.follow(category["link_category"], callback=self.parse(category["link_category"]))

        # print(content_file[0]["name_category"])
        # for category in content_file:
        #     print(category)
