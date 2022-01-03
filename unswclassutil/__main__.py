import sys
import mechanicalsoup

from bs4.element import Tag
from http import HTTPStatus
from requests.exceptions import HTTPError

from .helper import Helper


"""A small script to scrape UNSW Class Utilisation. 

UNSW Class Utilisation contains course capacity for all subject areas (e.g. COMP) and terms 
(Summer/Term 1/ Term 2/ Term 3).

unswclassutil will get all relevant rows for a specific course (e.g. COMP1511).
"""

URL = "http://classutil.unsw.edu.au/"  
EXIT_FAILURE = 1

def main():
    course_code = sys.argv[1].upper() # course e.g. COMP1511
    term = sys.argv[2].upper() # Summ/T1/T2/T3:

    browser = mechanicalsoup.StatefulBrowser()
    response = browser.open(URL)
    if response.status_code != HTTPStatus.OK:
        raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')

    response = browser.follow_link(f'COMP_{term}.html')
    if response.status_code != HTTPStatus.OK:
        raise HTTPError(f'Expected status code 200 but actual was {response.status_code}.')

    courses_table = browser.get_current_page().find_all('table')[2]
    


    course_table: Tag

    for row in courses_table.find_all('tr'):
        if Helper.is_course_header_row(row) and row.find('a', {'name':'COMP1511T1'}):
            # found beginning row of course table
            course_table = row
    
    row = course_table
    course_name = row.find_next('td').find_next('td').get_text()
    output = {
        course_code: {
            "course_name": course_name        
        }
    }

    while True:
        row = row.find_next('tr') 
        if Helper.is_course_class_row(row):
            ...
        elif Helper.is_course_summary_row(row):
            comp = row.find_next().get_text()
            sect = row.find_next().get_text()
            class_ = row.find_next().get_text()
            type = row.find_next().get_text()
            status = row.find_next().get_text()
            capacity = row.find_next().get_text()
            percent_full = row.find_next().get_text()
            times = row.find_next().get_text()
            my_dict = {
                "comp": comp,
                "sect": sect,
                "class": class_,
                "type": type,
                "status": status,
                "capacity": capacity,
                "percent_full": percent_full,
                "times": times,
            }
            output[course_code].update(my_dict)
        elif Helper.is_course_header_row(row):
            print("reached end of course table")
            break 
    
    print(output)

    #table_data = table.find_all('td', {'class':'cucourse'})


    #courses = {}
    #for i in range(0, len(table_data), 2):
    #    capacity_table_data = table_data[i].find_next('tr').find('td', {'class':'cu00'})
    #    if not capacity_table_data:
    #        capacity = "100%" # table data that are None are equal to 100%
    #    else:
    #        capacity = capacity_table_data.get_text().replace(u'\xa0', '')

    #    course_code = table_data[i].get_text().replace(u'\xa0', '')
    #    course_name = table_data[i+1].get_text()

    #    courses[course_code] = {"courseName": course_name, "capacity": capacity}
    #return courses

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} course term", file = sys.stderr)
        sys.exit(EXIT_FAILURE)
    main()
