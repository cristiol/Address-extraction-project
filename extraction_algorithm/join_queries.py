from regex_patterns import zipcode_regex_usa_states, uk_zipcode_regex
import re


def get_joined_query(street_regex, zipcode_regex):
    """
    Combines a street address regex with a zipcode to form a search query string.

    This function attempts to extract a zipcode from the provided zipcode_regex using predefined regular expressions for US and UK formats.
    If a match is found, it combines the street address regex with the extracted zipcode to form a final search query string.
    Otherwise, it simply combines the street address regex with the original zipcode string.

    Args:
        street_regex (str): The regular expression for the street address.
        zipcode_regex (str): The zipcode string.

    Returns:
        str: The combined search query string (street address + zipcode).
    """
    final_zipcode_regex_us = re.search(zipcode_regex_usa_states, zipcode_regex)
    final_zipcode_regex_uk = re.search(uk_zipcode_regex, zipcode_regex)

    if final_zipcode_regex_us:
        joined_query = street_regex + ' ' + final_zipcode_regex_us.group()
    elif final_zipcode_regex_uk:
        joined_query = street_regex + ' ' + final_zipcode_regex_uk.group()
    else:
        joined_query = street_regex + ' ' + zipcode_regex

    return joined_query



