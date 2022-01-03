from bs4.element import Tag

class Helper:
    """A utility class to identify and extract `bs4.element.Tag`."""
    @staticmethod
    def is_course_header_row(row: Tag) -> bool:
        return bool(row.find('td', {'class':'cucourse'}))

    @staticmethod
    def is_course_summary_row(row: Tag) -> bool:
        if not row.has_attr('class'):
            return False
        class_name = row['class'][0]
        return class_name == 'stub'

    @staticmethod
    def is_course_class_row(row: Tag) -> bool:
        if not row.has_attr('class'):
            return False
        class_name = row['class'][0]
        return class_name == 'rowHighlight' or class_name == 'rowLowlight'  

    @staticmethod
    def extract_course_header_row(row: Tag) -> dict:
        if not Helper.is_course_header_row(row):
            raise ValueError("Incorrect row type expecting course header row.")

        course_code = row.find_next('td').get_text().replace(u'\xa0', '')
        course_name = row.find_next('td').find_next('td').get_text()
        course_header = {
            course_code: {
                "course_name": course_name
            }
        }
        return course_header

    @staticmethod
    def extract_course_summary_row(row: Tag) -> dict:
        if not Helper.is_course_summary_row(row):
            raise ValueError("Incorrect row type expecting course summary row.")
        row = row.find_next()
        comp = row.get_text()
        row = row.find_next()
        sect = row.get_text()
        row = row.find_next()
        class_ = row.get_text()
        row = row.find_next()
        type = row.get_text()
        row = row.find_next()
        status = row.get_text()
        row = row.find_next()
        capacity = row.get_text()
        row = row.find_next()
        percent_full = row.get_text().replace(u'\xa0', '')
        row = row.find_next()
        times = row.get_text()
        course_summary = {
            "comp": comp,
            "sect": sect,
            "class": class_,
            "type": type,
            "status": status,
            "capacity": capacity,
            "percent_full": percent_full,
            "times": times,
        }
        return course_summary

    @staticmethod
    def extract_course_class_row(row: Tag) -> dict:
        if not Helper.is_course_class_row(row):
            raise ValueError("Incorrect row type expecting course class row.")
        row = row.find_next()
        comp = row.get_text()
        row = row.find_next()
        sect = row.get_text()
        row = row.find_next()
        class_ = row.get_text()
        row = row.find_next()
        type = row.get_text()
        row = row.find_next()
        status = row.get_text()
        row = row.find_next()
        capacity = row.get_text()
        row = row.find_next()
        percent_full = row.get_text().replace(u'\xa0', '')
        row = row.find_next()
        times = row.get_text()
        course_class = {
            "comp": comp,
            "sect": sect,
            "class": class_,
            "type": type,
            "status": status,
            "capacity": capacity,
            "percent_full": percent_full,
            "times": times,
        }
        return course_class
