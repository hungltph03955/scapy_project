import json

import scrapy
import re

base_url = 'https://gearvn.com'


class ProductSpider(scrapy.Spider):
    name = 'product'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('./data/category/data_category.json', 'r') as json_file:
            content_file = json.load(json_file)
            all_link = []
            for category in content_file:
                all_link.append(category["link_category"])

            self.start_urls = all_link

    def parse(self, response):
        print("response.request.url")
        print(response.request.url)

        data_link_page_product = {}
        all_link_page = []
        total_page = 0

        all_li_pagination = response.css('ul.pagination-list li.hidden-phone')
        for itemPagination in all_li_pagination:
            link_product = itemPagination.css('a.pagenav::attr(href)').extract_first()
            all_link_page.append(link_product)

        if len(all_link_page) > 0:
            last_page = all_link_page[-1]
            total_page = int(re.search(r'\d+', last_page).group(0))

        if total_page > 0:
            for i in range(total_page):
                link_page_product = str(response.request.url) + "?page=" + str(i + 1)
                data_link_page_product = {
                    'link_page_product': link_page_product,
                }
                print(data_link_page_product)
        else:
            data_link_page_product = {
                'link_page_product': response.request.url,
            }
            print(data_link_page_product)

            # yield data_link_page_product

            # with open('./data/category/data_category.json') as json_file:
            #     content_file = json.load(json_file)
            #     for category in content_file:
            #         yield response.follow(category["link_category"], callback=self.parse(category["link_category"]))

            # print(content_file[0]["name_category"])
            # for category in content_file:
            #     print(category)
