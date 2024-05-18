from get_final_addresses_by_one_list import get_final_addresses_by_one_list
from join_queries import get_joined_query
from transform_query_list_into_geocode import transform_query_list_into_geocode_address


def get_final_addresses_by_joined_query(query_1, query_2):
    """
    Identifies final addresses by combining queries from two lists and performing geocoding.

    This function takes two lists of queries (`query_1` and `query_2`). It iterates through all possible combinations
    of queries (one from each list) and attempts to create a joined query string using the `get_joined_query`
    function.

    If a valid joined query is formed, it's used to potentially retrieve geocoded addresses through an external function
    `transform_query_list_into_geocode_address`. The retrieved addresses are then passed to
    `get_final_addresses_by_one_list` to extract and merge final addresses.

    The function returns a list of final addresses if at least one address is found, otherwise it returns `None`.

    Args:
        query_1 (list): The first list of query strings.
        query_2 (list): The second list of query strings.

    Returns:
        list: A list of dictionaries containing the final, unique merged addresses, or None if no addresses are found.
    """
    joined_query_list = []

    for i in query_1:
        for j in query_2:
            joined_query_item = get_joined_query(i, j)

            if joined_query_item is not None:
                joined_query_list.append(joined_query_item)

    if len(joined_query_list) >= 1:
        final_addresses = get_final_addresses_by_one_list(transform_query_list_into_geocode_address(joined_query_list))

        return final_addresses

    else:
        return None

