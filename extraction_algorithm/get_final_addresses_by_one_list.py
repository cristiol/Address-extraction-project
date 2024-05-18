from mergging_dictionaries import set_final_address_value
from validate_final_addreess import validate_final_address


def transform_geopy_address_into_final_address(address_1):
    """
    Transforms a geopy address dictionary into a final address dictionary.

    This function takes a dictionary `address_1` (assumed to be a geopy address dictionary) and uses the `
    set_final_address_value` function to retrieve and set final address values based on a predefined mapping.
    It iterates over a dictionary `final_address_keys` that maps final address keys to priority keys (or key lists) in
    the geopy address dictionary.

    Args:
        address_1 (dict): The geopy address dictionary to transform.

    Returns:
        dict: A dictionary containing the final address with selected values.
    """

    final_address_keys = {
        "country": "country",
        "state": "state",
        "region": "county",
        "city": ["city", "town", "village", "municipality", "locality"],
        "postcode": "postcode",
        "road": "road",
        "road_numbers": "house_number",
    }

    final_address = {key: set_final_address_value(address_1, {}, final_address_keys[key])  # Use empty dict for address_2
                      for key in final_address_keys}
    if validate_final_address(final_address):
        return final_address
    else:
        return None


def get_final_addresses_by_one_list(address_list):
    """
    Identifies unique addresses from a single list of addresses and merges them.

    This function takes a list of address dictionaries (`address_list`) as input.
    It iterates through each address in the list and transforms it into a final address dictionary using
    the `transform_geopy_address_into_final_address` function (assumed to be defined elsewhere).
    The transformed addresses are stored in a list `final_addresses`.

    Finally, the function removes duplicate addresses from `final_addresses` using set logic.
    It converts each address dictionary into a tuple of key-value pairs and creates a set to eliminate duplicates.
    The unique addresses are then converted back into dictionaries and stored in `unique_address_list`.

    The function returns `unique_address_list` if it contains at least one address, otherwise it returns `None`.

    Args:
        address_list (list): A list of dictionaries containing addresses.

    Returns:
        list: A list of dictionaries containing the final, unique merged addresses, or None if no addresses are provided.
    """
    final_addresses = []

    for item in address_list:
        validated_item = transform_geopy_address_into_final_address(item)
        if validated_item is not None:
            final_addresses.append(validated_item)

    if len(final_addresses) >= 1:
        unique_addresses = set(tuple(d.items()) for d in final_addresses)
        unique_address_list = [dict(t) for t in unique_addresses]
        print('final unique addresses: ', unique_address_list)
    else:
        return None

    if len(unique_address_list) >= 1:
        return unique_address_list
    else:
        return None

