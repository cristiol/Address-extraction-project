from bs4 import BeautifulSoup
from fetch_url import fetch_website_content


def get_aux_link(link):

    response = fetch_website_content(link)
    if response:
        soup = BeautifulSoup(response, 'lxml')

        links = soup.find_all('a')
        for link in links:
            link_ = link.get('href')
            if 'contact' in str(link_).lower() or 'kontakt' in str(link_).lower():
                return link_
    else:
        return None

