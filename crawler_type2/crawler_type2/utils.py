from bs4 import BeautifulSoup
import unicodedata


def extract_text(html):
    soup = BeautifulSoup(html, "lxml")
    return unicodedata.normalize("NFKD", soup.get_text())
