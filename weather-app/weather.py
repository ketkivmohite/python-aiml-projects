# The `requests` library is the standard way to make HTTP requests in Python.
import requests

def get_weather(city_name):
    """Fetches weather data from a free weather API."""

    # The base URL for the weather API. We use a service that doesn't require an API key.
    # The format=j1 part tells it to give us data in the simple JSON format.
    # CORRECTED LINE: Ensure the URL has "//" after "https:"
    api_url = f"https://wttr.in/{city_name}?format=j1"

    try:
        # Make the request to the API
        response = requests.get(api_url)

        # This will raise an error if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # --- Extract the relevant information ---
        current_condition = data['current_condition'][0]
        city = data['nearest_area'][0]['areaName'][0]['value']
        region = data['nearest_area'][0]['region'][0]['value']
        country = data['nearest_area'][0]['country'][0]['value']
        
        # CORRECTED LINE: Using the proper newline character "\n"
        print("\n---  Current Weather ---")
        print(f"Location: {city}, {region}, {country}")
        print(f"Condition: {current_condition['weatherDesc'][0]['value']}")
        print(f"Temperature: {current_condition['temp_C']}°C")
        print(f"Feels Like: {current_condition['FeelsLikeC']}°C")
        print(f"Humidity: {current_condition['humidity']}%")
        print("--------------------------")

    except requests.exceptions.HTTPError as http_err:
        # This catches errors like "404 Not Found" which happens for invalid city names
        print(f"\nError: Could not find weather for '{city_name}'. Please check the city name.")
    except requests.exceptions.RequestException as err:
        # This catches other network-related errors (e.g., no internet connection)
        print(f"\nError: Something went wrong with the network request: {err}")
    except KeyError:
        # This catches errors if the JSON data is not in the expected format
        print("\nError: Could not parse the weather data.")


# --- Main Program Loop ---
def main():
    print("Welcome to the Python Weather App!")
    while True:
        city = input("\nEnter a city name to get the weather (or type 'exit' to quit): ")

        if city.lower() == 'exit':
            print("\nGoodbye!")
            break

        get_weather(city)

if __name__ == "__main__":
    main()






    