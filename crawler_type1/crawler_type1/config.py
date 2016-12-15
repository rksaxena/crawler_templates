SOURCES = {
    "valetmag": {
        "NAME": "valetmag",
        "ALLOWED_DOMAINS": "http://www.valetmag.com/",
        "START_URLS": [
            "http://www.valetmag.com/style/browser/browser-style_trends_all_visual.html"
        ],
        "XPATH": "//*[@id='entry']/a",
        "TEXT_XPATH": "p//text()",
        "IMG_XPATH": "img/@src"
    },
    "fashionbeans": {
        "NAME": "fashionbeans",
        "ALLOWED_DOMAINS": "http://www.fashionbeans.com",
        "START_URLS": [
            "http://www.fashionbeans.com/the-hot-list/"
        ],
        "XPATH": "//*[@class='hotList']/li",
        "TEXT_XPATH": "a//text()",
        "IMG_XPATH": "a/img/@src"
    },
    "fresherthanchris": {
        "NAME": "fresherthanchris",
        "ALLOWED_DOMAINS": "http://www.fresherthanchris.com/",
        "START_URLS": [
            "http://www.fresherthanchris.com/blog/"
        ],
        "XPATH": "//*[@class='post_wrapper']",
        "TEXT_XPATH": "div/p//text()",
        "IMG_XPATH": "a/img/@src"
    }
}
