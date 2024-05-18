from geopy_validation import get_geocode_address


def transform_query_list_into_geocode_address(queries):
    """
    Transforms a list of address queries into a list of geocoded addresses.

    This function iterates through a list of address queries (`queries`).
    For each unique query, it calls the `get_geocode_address` function to obtain the geocoded address information.
    It then filters out duplicates and returns a list of geocoded addresses, or None if no valid addresses are found.

    Args:
        queries (list): A list of address strings to geocode.

    Returns:
        list: A list of geocoded address dictionaries if found, otherwise None.
    """
    if queries is None:
        return None

    unique_queries = set(queries)

    geocode_addresses = []

    for query in unique_queries:
        geocode_address_item = get_geocode_address(query)

        if geocode_address_item is not None and geocode_address_item not in geocode_addresses:
            geocode_addresses.append(geocode_address_item)

    if geocode_addresses:
        return geocode_addresses
    else:
        return None


