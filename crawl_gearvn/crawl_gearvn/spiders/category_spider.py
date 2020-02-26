import scrapy


class CategorySpider(scrapy.Spider):
    """ scrapy crawl category -o data/category//data_category.json """
    name = 'category'

    start_urls = [
        'https://gearvn.com'
    ]

    def parse(self, response):
        all_div_category = response.css('div.freez ol.megamenu-nav-primary  li')
        for category in all_div_category:
            name_category = category.css('span.gearvn-cat-menu-name::text').extract()[0]
            link_category = category.css('a::attr(href)').extract()[0]
            data_category = {
                'name_category': name_category,
                'link_category': CategorySpider.start_urls[0] + link_category,
            }
            yield data_category
