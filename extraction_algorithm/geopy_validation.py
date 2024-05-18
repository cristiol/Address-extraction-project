from geopy.geocoders.nominatim import Nominatim
from regex_patterns import zipcode_regex_usa_states, uk_zipcode_regex, street_regex
import re
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable


def get_geocode_address(query):
    """
    Geocodes an address and returns a dictionary with location details.

    Args:
        query (str): The address to geocode.

    Returns:
        dict: A dictionary with location details or None on error.

    Raises:
        GeocoderError: General geocoding error.
    """

    geolocator = Nominatim(user_agent="Company-Location-Finder")

    try:
        # Extract US zip code from the query
        us_zipcode_match = re.search(zipcode_regex_usa_states, query)
        uk_zipcode_match = re.search(uk_zipcode_regex, query)
        street_match = re.search(street_regex, query)

        if us_zipcode_match:
            address = geolocator.geocode(query, addressdetails=True, timeout=3, country_codes="us")
            if not address:
                address = geolocator.geocode(us_zipcode_match.group(), addressdetails=True, timeout=3, country_codes="us")
        elif uk_zipcode_match:
            address = geolocator.geocode(query, addressdetails=True, timeout=3, country_codes="gb")
            if not address:
                address = geolocator.geocode(uk_zipcode_match.group(), addressdetails=True, timeout=3, country_codes="gb")
        else:
            if street_match:
                address = geolocator.geocode(street_match.group(), addressdetails=True, timeout=3)
            else:
                address = geolocator.geocode(query, addressdetails=True, timeout=2)

        return address.raw['address'] if address else None
    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"Geocoding error for {query}: {e}")
        return None

#
