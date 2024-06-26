# Approach and Thought Process

This section details the thought process behind developing this project and the steps taken to achieve the desired outcome.

## Initial Analysis

1. **Data Exploration:** The project began by extracting information from an input file containing 2479 URLs. Analyzing the file extensions revealed a predominance of `.com`, `.net`, `.org`, `.uk`, and `.de` extensions.This suggested a focus on extracting addresses from websites likely located in the US, UK, and Germany.

<p align="center">
<img src="https://github.com/cristiol/Address-extraction-project/assets/142798921/2539d98d-b8d6-49ac-a44c-5fbe9950a734">
</p>

2. **Address Format Analysis:**  Further analysis concentrated on address formats in these countries, particularly the US and UK. Identifiable patterns within these formats led to the development of regular expressions for extracting street addresses and zip codes.
<p align="center">
  <img src="https://github.com/cristiol/Address-extraction-project/assets/142798921/a7ad1260-6817-484a-a4f5-78f987ca3364">
</p>

3. **Website Analysis:** I analyzed as many websites as I could, and my conclusions were that the majority of addresses are presented on the website in a pretty standard way, and of course some websites don't work or don't have valid addresses.

##  Choosing an Approach

Based on the analysis, I decided to go for the regex approach, confident that I could get a good result with this approach.

##  Regular Expression Development

By taking a random website, the most likely address found is one from the US, then from the UK, then from Germany, and so on and so forth. I decided to make four [regex patterns](https://github.com/cristiol/Address-extraction-project/blob/main/extraction_algorithm/regex_patterns.py):

* **Street addresses** matches strings that contain a number, a street name, and a street type (e.g., 503 Maurice Street).
* **US zip codes** matches strings that contain a state name or abbreviation, a 5-digit number (e.g., NC 28112).
* **UK zip codes** matches strings that contain a pattern with one or two letters, followed by one or two digits, and optionally another letter, a mandatory space, or a single digit followed by two letters. (e.g., SW9 0FQ)
* **Regular zip codes** (for broader coverage) matches strings that contain groups of 5 digits (e.g., 28112).

##  Website Content Search Strategy

After some testing and deliberation, I decided the best approach is to search the content of the website by routes:

1. **Street Route:**  Prioritize searching for street addresses.
2. **Zip Code Route (Prioritized Order):**
    * Search for US zip codes (higher likelihood and lower false positive risk).
    * Search for UK zip codes.
    * Search for regular zip codes (as a last resort due to lower reliability).

##  Refining Regex Patterns

I did some tests to refine the regex patterns and was pretty happy with the results, but...

##  Data Transformation and Validation

How do I transform these strings from websites into the address format that I want, and how do I know if the address found is actually a valid address? 

After some research, documentation, and testing, I chose Geopy. I was really happy and kind of impressed with the efficacy of geopy.

However, limitations of Geopy were identified, such as:

* Reduced accuracy for street-only or simple zip code queries.
* Performance limitations due to inherent processing overhead.

But at least I have the certainty that I will receive valid addresses that actually exist and in a format I can work with.

(example of format)
<p align="center">
  <img src="https://github.com/cristiol/Address-extraction-project/assets/142798921/0f7f0bae-cacb-4724-a6bc-0f4022fb8b8f">
</p>

##  Maximizing Accuracy with Geopy

Now it's time to come up with some clever ideas to maximize the geopy and the accuracy of the results.

As far as I know, street-only queries and simple regular zip codes have lower accuracy, so this has to be the last resort.

But I notice something: when I query Geopy, I can set the country code, and then the accuracy is impressive, but how do I know when to set what? 

But... what if, in these queries I already have, I can search with regex patterns I already have, and then if there is a match, it must be that country, right?

So I came up with this [algorithm](https://github.com/cristiol/Address-extraction-project/blob/main/extraction_algorithm/geopy_validation.py).

##  Handling Multiple Addresses

So far, so good, but another problem: what if there are many addresses? How do I know which is which?

I found two solutions.Both sound good to me, so I have to use them both.

1. **Compatibility Check:** Addresses extracted using street and zip code queries were compared for compatibility, If they are compatible, then merge.
2. **Joining Queries:** Street and zip code queries were combined and then generate the geopy address.

First the compability test, and then the joining queries method if the first failed.

I did some more testing and made some touches here and there, and now it's time to design the main script and find the best way to maximize the result.

##  Main Script Design

The main script was designed to:

1. Check the status code of retrieved URLs.
2. Parse website content using BeautifulSoup.
3. Search for addresses using the defined order of regex patterns (street first, then zip codes).
4. Follow two main paths based on the number of address lists generated by the regex search:
    * **One List Path:** Used for scenarios with only a street address or zip code query result.
    * **Two List Path:** Used for scenarios with both street address and zip code query results. This path involved:
        * Compatibility check between street and zip code addresses.
        * Joining queries if compatibility check failed.
        * Using the zip code query list over street query list(due to higher reliability based on testing) for geocoding as a last resort.
5. If an address was found on a separate webpage (e.g., contact page), the script would attempt to locate that page and process it as well.

##  Results

* From **2479** URLs, addresses were successfully extracted from **965 (38.92%)**, yielding a total of **1171** addresses.

##  Potential Issues

* Limitations of regex for handling edge cases and non-English addresses.
* Potential for false positives due to the use of regex.
* Increased processing time associated with Geopy usage.

##  Future Improvements

* Of course, the result can be improved, but I think to maximize efficiency, a mixed approach between traditional rule-based regex and some machine learning algorithms is needed.

##  Conclusion

Overall, I am very happy with the result, and confidently, I can say that I made a project of which I am proud.

# Installation

### Prerequisites

Ensure you have Python 3.6 or higher and Pip installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

**Installing Pip:**

If you don't have Pip installed, you can usually install it using the following command in your terminal:

```bash
python3 -m ensurepip --upgrade
```

### Install Dependencies

Once you have Python and Pip set up, you can install the required libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command will install the necessary dependencies listed in a file named `requirements.txt`. This file typically specifies libraries like BeautifulSoup4 for parsing HTML content and Geopy for geocoding addresses.


### Run the Program

```bash
python main_script.py
```

## Output

The program generates a JSON file named `output.json` containing the extracted addresses. Each address is represented as a JSON object with the following fields:

* **country:** The country code (e.g., "US", "UK").
* **region:** The administrative region (e.g., "California", "London"). (This may not always be available)
* **state:** The state or province  (This may not always be available depending on the address format)
* **city:** The city or town.
* **postcode:** The postal code or ZIP code.
* **street:** The street name.
* **street_number:** The street number.

## Example Output

<p align="center">
  <img src="https://github.com/cristiol/Address-extraction-project/assets/142798921/4554aa99-b56c-494b-9213-ff0fbe347bad">
</p>







