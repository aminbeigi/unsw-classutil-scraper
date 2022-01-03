import sys
import json
import humps

from bs4.element import Tag

from .helper import Helper
from .webscraper import WebScraper


"""A small script to scrape UNSW Class Utilisation. 

UNSW Class Utilisation contains course capacity for all subject areas (e.g. COMP) in each term 
(i.e. U1/T1/T2/T3).

unswclassutil will get all relevant rows for a specific COMP course (e.g. COMP1511), store it
in JSON format and output into a specified file.
Currently only scrapes subject area of COMP (computer science) but can be easily extended to
scrape other subject areas aswell.
"""

EXIT_FAILURE = 1
COURSES_TABLE = 2

def main():
    course_code = sys.argv[1].upper() # e.g. COMP1511
    term = sys.argv[2].upper() # U1|T1|T2|T3
    output_file_path = sys.argv[3]

    browser = WebScraper.browser(term)
    courses_table = browser.get_current_page().find_all('table')[COURSES_TABLE]

    course_table: Tag = None
    for row in courses_table.find_all('tr'):
        name = course_code + term
        if Helper.is_target_course_table(row, name):
            course_table = row

    if not course_table:
        raise ValueError(f'Did not find course table for course code {course_code} in term {term}')
    
    row = course_table
    output = {}
    course_header = Helper.extract_course_header_row(row)
    output.update(course_header)

    while True:
        row = row.find_next('tr') 
        if Helper.is_course_summary_row(row):
            course_summary = Helper.extract_course_summary_row(row)
            enrolment_type = course_summary['enrolment_type']
            output[course_code][enrolment_type] = {}
            output[course_code][enrolment_type] = course_summary
            output[course_code][enrolment_type]["classes"] = []
        elif Helper.is_course_class_row(row):
            course_class = Helper.extract_course_class_row(row)
            enrolment_type = course_summary['enrolment_type']
            output[course_code][enrolment_type]["classes"].append(course_class)
        elif Helper.is_course_header_row(row):
            # reached end of course table
            break 
    
    with open(output_file_path, 'w') as f:
        json.dump(humps.camelize(output), f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} course term output_file_path", file = sys.stderr)
        sys.exit(EXIT_FAILURE)
    main()
