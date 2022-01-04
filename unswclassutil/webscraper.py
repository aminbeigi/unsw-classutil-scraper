from http import HTTPStatus
from requests.exceptions import HTTPError
from mechanicalsoup import StatefulBrowser

class WebScraper:
    """A utility class to help with webscraping."""
    _BASE_URL = "http://classutil.unsw.edu.au/"  

    @staticmethod
    def browser(term: str) -> StatefulBrowser:
        """Initialise a browser on the correct page.

        Args:
            term: A UNSW term i.e. U1|T1|T2|T3.

        Returns:
            A StatefulBrowser.
        
        Raises:
            HTTPError: An unexpected HTTP status code when trying to access page.
        """
        browser = StatefulBrowser()
        response = browser.open(WebScraper._BASE_URL + f'COMP_{term}.html')
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(f"Unexpected status code trying to access {WebScraper._BASE_URL}/COMP_{term}.html."
                            f"Expected status code is 200 but actual was {response.status_code}.")
        return browser