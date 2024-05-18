import concurrent.futures
from fetch_url import fetch_website_content
from regex_patterns import street_regex, zipcode_regex_usa_states, uk_zipcode_regex, simple_zipcode_regex
from search_by_regex import search_by_regex
from get_final_addresses_by_two_list import get_final_addresses_by_two_list
from get_final_addresses_by_one_list import get_final_addresses_by_one_list
from transform_query_list_into_geocode import transform_query_list_into_geocode_address
from get_final_addresses_by_joined_query import get_final_addresses_by_joined_query
from append_to_json_file import append_to_json_file
from get_aux_links import get_aux_link
from extract_from_input_files.links import links


def get_address(link, recursion_count=0):
  response = fetch_website_content(link)

  street_address_by_regex = search_by_regex(response, street_regex)
  zipcode_addresses_by_regex = search_by_regex(response, zipcode_regex_usa_states)

  if zipcode_addresses_by_regex is None:
    zipcode_addresses_by_regex = search_by_regex(response, uk_zipcode_regex)
    if zipcode_addresses_by_regex is None:
      zipcode_addresses_by_regex = search_by_regex(response, simple_zipcode_regex)

  geocode_street_addresses = transform_query_list_into_geocode_address(street_address_by_regex)  # list of geocode addresses
  geocode_zipcode_addresses = transform_query_list_into_geocode_address(zipcode_addresses_by_regex)

  if street_address_by_regex is None and zipcode_addresses_by_regex is None:
    aux_link = get_aux_link(link)
    if aux_link and recursion_count < 1:
      return get_address(aux_link, recursion_count + 1)
    else:
      return None

  if geocode_street_addresses and geocode_zipcode_addresses:
    #print('----')
    #print('two list root')
    final_result = get_final_addresses_by_two_list(geocode_street_addresses, geocode_zipcode_addresses)
    if final_result:
      return append_to_json_file({'link': link.strip('https://'), 'address': final_result})

    if final_result is None:
      #print('---')
      #print('joined query rout')
      if get_final_addresses_by_joined_query(street_address_by_regex, zipcode_addresses_by_regex):
        #print('---')
        #print('zipcode route')
        final_result = get_final_addresses_by_joined_query(street_address_by_regex, zipcode_addresses_by_regex)
        if final_result:
          return append_to_json_file({'link': link.strip('https://'), 'address': final_result})
        elif get_final_addresses_by_one_list(geocode_zipcode_addresses):
          final_result = get_final_addresses_by_one_list(geocode_zipcode_addresses)
          return append_to_json_file({'link': link.strip('https://'), 'address': final_result})
        else:
          return None


  if geocode_street_addresses and geocode_zipcode_addresses is None:
    #print('----')
    #print('street regex rout')
    if get_final_addresses_by_one_list(geocode_street_addresses):
      final_result = get_final_addresses_by_one_list(geocode_street_addresses)
      if final_result:
        return append_to_json_file({'link': link.strip('https://'), 'address': final_result})

  if geocode_street_addresses is None and geocode_zipcode_addresses:
    #print('---')
    #print('zipcode route')
    if get_final_addresses_by_one_list(geocode_zipcode_addresses):
      final_result = get_final_addresses_by_one_list(geocode_zipcode_addresses)
      if final_result:
        return append_to_json_file({'link': link.strip('https://'), 'address': final_result})
    else:
      return None



# with concurrent.futures.ThreadPoolExecutor() as executor:
#    results = list(executor.map(get_address, links[250:300]))

for link in links[:3]:
    get_address(link)
    print('index: ', links.index(link))
#print(get_address('https://lrgmarketing.com/'))