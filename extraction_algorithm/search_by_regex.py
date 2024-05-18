import re
from bs4 import BeautifulSoup


def search_by_regex(text, regex):
    """
    Extracts addresses from the given text using the provided regular expression.

    Args:
        text (str): The text to search for  addresses.
        regex (str): A regular expression pattern to match addresses.

    Returns:
        list: A list of extracted addresses (strings) if found, otherwise None.

    Raises:
        Exception: If an error occurs during parsing with BeautifulSoup.
    """
    try:
        soup = BeautifulSoup(text, 'lxml')
        addresses_found = [val.strip() for val in soup.find_all(string=regex) if len(val) <= 100]
        if addresses_found:
            return addresses_found
        else:
            return None
    except Exception as e:
        #print(f'Error parsing text: {e}')
        return None





