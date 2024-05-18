from check_compability import check_compatibility_geopy_addresses
from mergging_dictionaries import merging_addresses_into_final_address


def get_final_addresses_by_two_list(address_1_list, address_2_list):
    """
        Identifies compatible address combinations from two lists and merges them.

        This function takes two lists of addresses (address_1_list and address_2_list) as input.
        It iterates through each combination of addresses (one from each list) and checks their compatibility using an
        external function `check_compatibility_geopy_addresses`.
        If the addresses are compatible, it merges them into a final address dictionary using the
        `merging_addresses_into_final_address` function.
        The merged addresses are stored in a list `final_addresses`.

        Finally, the function removes duplicate addresses from `final_addresses` using set logic.
        It converts each address dictionary into a tuple of key-value pairs and creates a set to eliminate duplicates.
        The unique addresses are then converted back into dictionaries and stored in `unique_address_list`.

        The function returns `unique_address_list` if it contains at least one address, otherwise it returns `None`.

        Args:
            address_1_list (list): The first list of address dictionaries.
            address_2_list (list): The second list of address dictionaries.

        Returns:
            list: A list of dictionaries containing the final, unique merged addresses, or None if no compatible addresses are found.
        """

    final_addresses = []

    for i in address_1_list:
        for j in address_2_list:

            if check_compatibility_geopy_addresses(i, j) is True:
                validated_item = merging_addresses_into_final_address(i,j)
                if validated_item is not None:
                    final_addresses.append(validated_item)


    unique_addresses = set(tuple(d.items()) for d in final_addresses)
    unique_address_list = [dict(t) for t in unique_addresses]

    print('final unique addresses', unique_address_list)
    if len(unique_address_list) >= 1:
        return unique_address_list
    else:
        return None





