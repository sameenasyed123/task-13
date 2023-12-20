import requests

def display_country_info():
    api_url = "https://restcountries.com/v3.1/all"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            countries_data = response.json()

            # Display information for each country
            for country_data in countries_data:
                name = country_data['name']['common']
                currencies = country_data['currencies']
                
                print(f"Country: {name}")
                print("Currencies:")
                
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info['name']
                    currency_symbol = currency_info['symbol'] if 'symbol' in currency_info else 'N/A'
                    
                    print(f"  {currency_name} ({currency_code}): {currency_symbol}")

                print("\n" + "="*30 + "\n")  # Separating each country's information

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the method to display country information
display_country_info()
