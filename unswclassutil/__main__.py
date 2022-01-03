import sys

from bs4.element import Tag

from .helper import Helper
from .webscraper import WebScraper


"""A small script to scrape UNSW Class Utilisation. 

UNSW Class Utilisation contains course capacity for all subject areas (e.g. COMP) and terms 
(Summer/Term 1/ Term 2/ Term 3).

unswclassutil will get all relevant rows for a specific course (e.g. COMP1511).
"""

EXIT_FAILURE = 1
COURSES_TABLE = 2

def main():
    course_code = sys.argv[1].upper() # course e.g. COMP1511
    term = sys.argv[2].upper() # Summ/T1/T2/T3:

    browser = WebScraper.browser(term)
    courses_table = browser.get_current_page().find_all('table')[COURSES_TABLE]

    course_table: Tag
    for row in courses_table.find_all('tr'):
        name = course_code + term
        if Helper.is_course_header_row(row) and row.find('a', {'name': name}):
            # found first row of target course table
            course_table = row
    
    row = course_table
    output = {}
    output.update(Helper.extract_course_header_row(row))
    output[course_code]["classes"] = []

    while True:
        row = row.find_next('tr') 
        if Helper.is_course_class_row(row):
            output[course_code]["classes"].append(Helper.extract_course_class_row(row))
        elif Helper.is_course_summary_row(row):
            output[course_code].update(Helper.extract_course_summary_row(row))
        elif Helper.is_course_header_row(row):
            # reached end of course table
            break 
    print(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} course term", file = sys.stderr)
        sys.exit(EXIT_FAILURE)
    main()
