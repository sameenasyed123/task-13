import requests

class CountryApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_all_data(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    # Specify the API URL
    api_url = "https://restcountries.com/v3.1/all"
    
    # Create an instance of the CountryApiClient with the provided URL
    country_api = CountryApiClient(api_url)

    # Fetch all data
    all_data = country_api.fetch_all_data()

    if all_data:
        # Process the data as needed
        print(all_data)
    else:
        print("Failed to fetch data.")
