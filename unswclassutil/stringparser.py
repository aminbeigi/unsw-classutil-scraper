class StringParser:
    """A utility class to parse strings extracted from `bs4.element.Tag`."""
    @staticmethod
    def parse_times_string(string: str) -> list:
        """Parse a 'times' string

        Args:
            string: A string. For example: 'Fri 09 (w1-5,7-8,10, Quad G046); Fri 10-12 (w1-5,7-8,10, BrassME305)'

        Returns:
            A list of times.
        """
        return string.split('; ')