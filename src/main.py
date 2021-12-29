import sys
from http import HTTPStatus
from requests.exceptions import HTTPError
import mechanicalsoup

"""
A small script to scrape UNSW Class Utilisation. 
UNSW Class Utilisation contains course capacity for all subject areas (e.g. COMP) and terms 
(Summer/Term 1/ Term 2/ Term 3).
"""

URL = "http://classutil.unsw.edu.au/"  
EXIT_FAILURE = 1

def main() -> dict:
    course = sys.argv[1].upper() # course e.g. COMP
    term = sys.argv[2].upper() # Summ/T1/T2/T3:

    browser = mechanicalsoup.StatefulBrowser()
    response = browser.open(URL)
    if response.status_code != HTTPStatus.OK:
        raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')

    response = browser.follow_link(f'{course}_{term}.html')
    if response.status_code != HTTPStatus.OK:
        raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')

    table = browser.get_current_page().find_all('table')[2]
    table_data = table.find_all('td', {'class':'cucourse'})

    courses = {}
    for i in range(0, len(table_data), 2):
        capacity_table_data = table_data[i].find_next('tr').find('td', {'class':'cu00'})
        if not capacity_table_data:
            capacity = "100%" # table data that are None are equal to 100%
        else:
            capacity = capacity_table_data.get_text().replace(u'\xa0', '')

        course_code = table_data[i].get_text().replace(u'\xa0', '')
        course_name = table_data[i+1].get_text()

        courses[course_code] = {"courseName": course_name, "capacity": capacity}
    return courses

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} course term", file = sys.stderr)
        sys.exit(EXIT_FAILURE)
    main()