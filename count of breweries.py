import requests
from collections import defaultdict

def get_brewery_count_by_state():
    api_url = "https://api.openbrewerydb.org/breweries"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            breweries_data = response.json()

            # Count breweries in each state
            state_brewery_count = defaultdict(int)
            for brewery_data in breweries_data:
                state = brewery_data.get('state', '').lower()
                state_brewery_count[state] += 1

            # Display brewery count for each state
            print("Brewery count in each state:")
            for state, count in state_brewery_count.items():
                print(f"{state.capitalize()}: {count} breweries")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the method to display brewery count in each state
get_brewery_count_by_state()
