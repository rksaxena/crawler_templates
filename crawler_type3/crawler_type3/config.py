SOURCES = {
    "zara_india": {
        "NAME": "zara_india",
        "ALLOWED_DOMAINS": "http://www.zara.com/",
        "START_URLS": [
            "http://www.zara.com/in/"
        ],
        "BASE_URL": "http:",
        "CATEGORY_XPATH": "//*[@id='menu']/ul/li[1]/ul/li/a/@href",
        "LIST_PAGE_XPATH": "//ul[contains(@class,'_subcategories current')]/li/a/@href",
        "ELEMENTS_XPATH": "//ul[contains(@class,'product-list')]/li",
        "HEADING_XPATH": "//div[contains(@class,'NO_HEADING_XXX')]",
        "TEXT_XPATH": "div/a/text()",
        "IMG_XPATH": "a/img/@src"
    }
}
