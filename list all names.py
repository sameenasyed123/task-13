import requests

def get_breweries_by_state(states):
    api_url = "https://api.openbrewerydb.org/breweries"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            breweries_data = response.json()

            # Filter and display breweries in the specified states
            print("Breweries in the specified states:")
            for brewery_data in breweries_data:
                state = brewery_data.get('state', '').lower()

                if state in states:
                    name = brewery_data.get('name', 'N/A')
                    print(f"{name} - {state}")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the states you are interested in
desired_states = {'alaska', 'maine', 'new york'}

# Call the method to display breweries in the specified states
get_breweries_by_state(desired_states)
