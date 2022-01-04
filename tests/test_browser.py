import pytest

from requests.exceptions import HTTPError

from unswclassutil.webscraper import WebScraper

def test_init_browser_raises_no_error():
    term = "U1"
    WebScraper.browser(term)

    term = "T1"
    WebScraper.browser(term)

    term = "T2"
    WebScraper.browser(term)

    term = "T3"
    WebScraper.browser(term)

def test_init_browser_raises_error():
    term = "batman"
    with pytest.raises(HTTPError):
        WebScraper.browser(term)