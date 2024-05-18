from validate_final_addreess import validate_final_address


def set_final_address_value(address_1, address_2, key):
    """
    Selects and returns a final address value based on priority from two dictionaries.

    This function takes two dictionaries (address_1 and address_2) and a key (or list of keys) representing an address component.
    It tries to retrieve the value for the key from address_1 first. If not found or empty, it attempts to retrieve the value
    from address_2. If no value is found in either dictionary, it returns an empty string.

    Args:
        address_1 (dict): The first dictionary containing address components.
        address_2 (dict): The second dictionary containing address components.
        key (str or list): The address component key or a list of alternative keys to try.

    Returns:
        str: The final address value (from address_1 or address_2), or an empty string if not found.
    """

    if isinstance(key, str):
        # Try address_1 first, then address_2
        return address_1.get(key, address_2.get(key, ""))
    elif isinstance(key, list):
        # Try each key in the list from address_1, then address_2
        for k in key:
            value = address_1.get(k)
            if value:
                return value
        return address_2.get(k, "")
    else:
        raise ValueError("Invalid key type: {}".format(type(key)))  # Raise error for unexpected key type


def merging_addresses_into_final_address(address_1, address_2):
    """
    Merges address components from two dictionaries into a final address dictionary.

    This function takes two dictionaries (address_1 and address_2) assumed to contain address components.
    It iterates over a predefined dictionary mapping final address keys to priority keys (or key lists) in the input dictionaries.
    For each final address key, it calls `set_final_address_value` to retrieve and set the corresponding value in the final address.

    Args:
        address_1 (dict): The first dictionary containing address components.
        address_2 (dict): The second dictionary containing address components.

    Returns:
        dict: A dictionary containing the final merged address with selected values.
    """

    final_address_keys = {
        "country": "country",
        "state": "state",
        "region": "county",
        "city": ["city", "town", "village", "municipality", "locality"],
        "postcode": "postcode",
        "road": "road",
        "road_numbers": ["house_number", "road_numbers"],
    }

    final_address = {key: set_final_address_value(address_1, address_2, final_address_keys[key])
                      for key in final_address_keys}
    if validate_final_address(final_address):
        return final_address
    else:
        return None







