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
    # Input the API URL through the constructor
    api_url = input("Enter the API URL: ")
    
    # Create an instance of the CountryApiClient with the provided URL
    country_api = CountryApiClient(api_url)

    # Example: Get all countries
    countries_data = country_api.get_all_countries()

    if countries_data:
        # Process the data as needed
        for country in countries_data:
            print(country)
    else:
        print("Failed to fetch country data.")
