from bs4.element import Tag

class Helper:
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
