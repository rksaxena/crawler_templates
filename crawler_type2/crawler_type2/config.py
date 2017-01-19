SOURCES = {
    "vogue_india": {
        "NAME": "vogue_india",
        "ALLOWED_DOMAINS": "http://www.vogue.in/",
        "START_URLS": [
            "http://www.vogue.in/fashion/fashion-trends/"
        ],
        "BASE_URL": "http://www.vogue.in/",
        "LIST_PAGE_XPATH": "//*[@id='eight_grid_block0']/section/div[1]/h3/a/@href",
        "BLOG_CONTENT_XPATH": "//div[contains(@class,'description')]",
        "HEADING_XPATH": "//div[contains(@class,'midContent')]/article/h1/text()",
        "TEXT_XPATH": "//div[contains(@class,'midContent')]/article/div[1]/p/text()",
        "IMG_XPATH": "//div[contains(@class,'cycle-slideshow')]//img/@src"
    },
    "stylegirlfriend": {
        "NAME": "stylegirlfriend",
        "ALLOWED_DOMAINS": "http://www.stylegirlfriend.com/",
        "START_URLS": [
            "http://www.stylegirlfriend.com/blog/"
        ],
        "BASE_URL": "",
        "LIST_PAGE_XPATH": "//div[contains(@class,'post-header-area')]//a[2]/@href",
        "HEADING_XPATH": "//div[contains(@class,'NO-HEADING-XXX')]",
        "BLOG_CONTENT_XPATH": "//div[contains(@class,'blog-post')]",
        "TEXT_XPATH": "p//text()",
        "IMG_XPATH": "//div[contains(@class,'blog-img')]//img/@src"
    },
    "gq-magazine": {
        "NAME": "gq-magazine",
        "ALLOWED_DOMAINS": "http://www.gq-magazine.co.uk/",
        "START_URLS": [
            "http://www.gq-magazine.co.uk/topic/fashion"
        ],
        "BASE_URL": "http://www.gq-magazine.co.uk",
        "LIST_PAGE_XPATH": "//div[contains(@class,'c-card-list__item')]/article/a/@href",
        "HEADING_XPATH": "//article[1]/div[1]/div[1]/h1/text()",
        "BLOG_CONTENT_XPATH": "//article[1]/div[2]/div/div",
        "TEXT_XPATH": "string(.)",
        "IMG_XPATH": "//figure/div/img/@data-src"
    },
    "whowhatwear": {
        "NAME": "whowhatwear",
        "ALLOWED_DOMAINS": "http://www.whowhatwear.com/",
        "START_URLS": [
            "http://www.whowhatwear.com/section/fashion-trends"
        ],
        "BASE_URL": "http://www.whowhatwear.com/",
        "LIST_PAGE_XPATH": "//div[@class='promo-feed-img']/a/@href",
        "HEADING_XPATH": "//div[contains(@class,'widgets-list-headline')]/h1/text()",
        "BLOG_CONTENT_XPATH": "//article[1]/div[2]/div/div",
        "TEXT_XPATH": "//div[contains(@class,'body')]/p//text()",
        "IMG_XPATH": "//div[contains(@class,'image-container')]/img/@src"
    }
}
