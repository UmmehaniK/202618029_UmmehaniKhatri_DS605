import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):

        # Visit every book on the current page
        for book in response.css("article.product_pod"):
            detail_url = response.urljoin(book.css("h3 a::attr(href)").get())
            yield scrapy.Request(detail_url, callback=self.parse_book)

        # Go only to pages 2,3,4,5
        current_page = int(
            response.url.split("page-")[-1].replace(".html", "")
        )

        if current_page < 5:
            next_page = response.css("li.next a::attr(href)").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):

        availability = "".join(
            response.css("p.instock.availability::text").getall()
        ).strip()

        category = response.css("ul.breadcrumb li a::text").getall()
        if len(category) >= 3:
            category = category[2]
        else:
            category = ""

        description = response.css("#product_description + p::text").get()

        yield {
            "title": response.css("div.product_main h1::text").get(),
            "category": category,
            "price": response.css("p.price_color::text").get(),
            "rating": response.css("p.star-rating::attr(class)").get().replace("star-rating ", ""),
            "availability": availability,
            "description": description,
            "upc": response.xpath('//th[text()="UPC"]/following-sibling::td/text()').get(),
            "number_of_reviews": response.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()').get(),
            "product_url": response.url,
        }