import requests


def fetch_website_content(url):
    """Fetches the content of a website using requests.

    This function makes a GET request to the specified URL and returns the website's HTML content as a string.
    If an error occurs during the request, it prints an error message and returns None.

    Args:
        url (str): The URL of the website to fetch content from.

    Returns:
        str: The HTML content of the website, or None if an error occurs.
    """
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"})
        print(f"GET request to {url} returned status code: {response.status_code}")
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website content: {e}")
        return None


