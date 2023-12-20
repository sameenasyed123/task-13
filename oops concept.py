#https://restcountries.com/v3.1/all,
#using the oops concept for the following task

import requests

class CountryApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_countries(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    api_url = "https://restcountries.com/v3.1/all"
    country_api = CountryApiClient(api_url)

    # Example: Get all countries
    countries_data = country_api.get_all_countries()

    if countries_data:
        # Process the data as needed
        for country in countries_data:
            print(country)
    else:
        print("Failed to fetch country data.")
