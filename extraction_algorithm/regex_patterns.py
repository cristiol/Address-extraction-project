import re

street_regex = re.compile(r"(?i)(^|\s)\d{2,7}\b\s+.{3,30}\b\s+((?:road|rd|way|hwy|street|st|str|avenue|ave|boulevard|blvd|lane|ln|drive|dr|terrace|ter|place|pl|court|ct|straße|allee|all|platz|weg|ring|damm|ufer|berg|tal|park|)\b\s*){1,}(?:\.|,|\s|$)")

zipcode_regex_usa_states = re.compile( r"(?i)(?<!\S)(?:\b)(ALABAMA|ALASKA|ARIZONA|ARKANSAS|CALIFORNIA|COLORADO|CONNECTICUT|DELAWARE|FLORIDA|GEORGIA|HAWAII|IDAHO|ILLINOIS|INDIANA|IOWA|KANSAS|KENTUCKY|LOUISIANA|MAINE|MARYLAND|MASSACHUSETTS|MICHIGAN|MINNESOTA|MISSISSIPPI|MISSOURI|MONTANA|NEBRASKA|NEVADA|NEW HAMPSHIRE|NEW JERSEY|NEW MEXICO|NEW YORK|NORTH CAROLINA|NORTH DAKOTA|OHIO|OKLAHOMA|OREGON|PENNSYLVANIA|RHODE ISLAND|SOUTH CAROLINA|SOUTH DAKOTA|TENNESSEE|TEXAS|UTAH|VERMONT|VIRGINIA|WASHINGTON|WEST VIRGINIA|WISCONSIN|WYOMING|AL|AK|AZ|AR|CA|CO|CT|DE|DC|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\s+(?:,\s*)?[0-9]{5}(?!\d)(?:-\d{4}(?!\d))?")

simple_zipcode_regex = re.compile(r"(?<!\S)(\d{5})(?!\S)")

uk_zipcode_regex = re.compile(r"\b[A-Z]{1,2}\d{1,2}[A-Z]?\s+\d[A-Z]{2}\b")

"""
1. street_regex
This regex is designed to match street addresses. It includes:

An optional leading whitespace or start of the string.
A number with 2 to 7 digits (the street number).
A street name with 3 to 30 characters.
A street type (e.g., Road, Rd, Street, St, Avenue, Ave, Boulevard, Blvd, etc.), with optional whitespace after.
An optional period, comma, whitespace, or end of the string.
The street types supported include common abbreviations and variations for roads, streets, avenues, boulevards, lanes, drives, terraces, places, courts, and several German equivalents.

2. zipcode_regex_usa_states
This regex is used to match US addresses that include both the state name (full or abbreviated) and a valid US ZIP code. It features:

A list of US states (both full names and abbreviations).
Optional whitespace and comma separation.
A five-digit ZIP code, with an optional extended ZIP+4 part (separated by a hyphen).
3. simple_zipcode_regex
This regex is used to match simple five-digit US ZIP codes. It includes:

A five-digit number.
Boundaries to ensure the ZIP code is not part of a longer string of digits (using negative lookbehind and negative lookahead assertions).
4. uk_zipcode_regex
This regex is used to match UK postal codes. It includes:

A pattern with one or two letters, followed by one or two digits, and optionally another letter.
A mandatory space.
A single digit followed by two letters.
This format captures the structure of UK postcodes, which typically include a district code, a space, and a unit code.
"""







