import mechanicalsoup

from http import HTTPStatus
from requests.exceptions import HTTPError

class WebScraper:
    """A utility class to help with webscraping."""
    _URL = "http://classutil.unsw.edu.au/"  

    @staticmethod
    def browser(term: str) -> mechanicalsoup.StatefulBrowser:
        browser = mechanicalsoup.StatefulBrowser()
        response = browser.open(WebScraper._URL)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')

        response = browser.follow_link(f'COMP_{term}.html')
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')
        return browser
