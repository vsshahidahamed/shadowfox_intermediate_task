import requests
from bs4 import BeautifulSoup

def scrape_countries():
    """
    Scrapes country names and capitals from https://www.scrapethissite.com/pages/simple/
    """
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all country containers
    countries = soup.find_all('div', class_='col-md-4 country')

    for country in countries:
        # Extract the country name
        name_element = country.find('h3', class_='country-name')
        if name_element:
            name = name_element.get_text(strip=True)
        else:
            name = "No name found"

        # Extract the capital
        capital_element = country.find('span', class_='country-capital')
        if capital_element:
            capital = capital_element.get_text(strip=True)
        else:
            capital = "No capital found"

        print(f"{name}: {capital}")

if __name__ == "__main__":
    scrape_countries()
