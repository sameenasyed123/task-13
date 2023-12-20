import requests

def display_countries_with_dollar():
    api_url = "https://restcountries.com/v3.1/all"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            countries_data = response.json()

            # Display countries with Dollar as currency
            print("Countries with Dollar as Currency:")
            for country_data in countries_data:
                currencies = country_data.get('currencies', {})
                
                # Check if USD is in the list of currencies
                if 'USD' in currencies:
                    name = country_data['name']['common']
                    print(f"{name}")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the method to display countries with Dollar as currency
display_countries_with_dollar()
