import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve API key
API_KEY = os.getenv("API_KEY")


def select_location(locations):
    """Asks the user to select a location if multiple results exist."""
    if len(locations) == 1:
        return locations[0]  # Only one option available

    print("\nMultiple locations found. Please select the correct one:")
    index = 1  # Manual counter variable
    for loc in locations:
        print(f"{index}: {loc['name']}, {loc['country']} "
              f"(Lat: {loc['latitude']}, Lon: {loc['longitude']})")
        index += 1  # increment manually

    choice = input("Enter the number of your city: ").strip()

    if choice.isdigit():
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(locations):
            return locations[choice_index]

    print("Invalid selection. Exiting program.")
    exit()


class WeatherApp:
    def __init__(self, city):
        self.city = city
        self.lat = None
        self.lon = None
        self.temperature = None

    def get_coordinates(self):
        """ Fetch latitude and longitude of self.city using API Ninjas."""

        url = f"https://api.api-ninjas.com/v1/geocoding?city={self.city}"
        params = {"city": self.city, "X-Api-Key": API_KEY}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if not data:
                print(f"Error: No location found for {self.city}")
                return
            # Let the user pick the correct location if there are multiple results
            selected_location = select_location(data)

            # Store the coordinates
            self.lat = selected_location["latitude"]
            self.lon = selected_location["longitude"]

        else:
            print("Error: Could not retrieve coordinates.")

    def get_weather(self):
        """fetch current weather data"""
        if self.lat is None or self.lon is None:
            print("Error: Cannot get weather without coordinates.")
            return

        """Fetches current weather data using Open-Meteo API."""
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "current_weather": True
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            self.temperature = data["current_weather"]["temperature"]

    def suggest_clothing(self):
        """Prints Pezhman's weather-based comments."""
        if self.temperature is None:
            print("Error: No temperature data available.")
            return

        if self.temperature < 0:
            print("Pezhman says: 'F**king freezzzyyy! Stay at home! 🥶'")

        if self.temperature < 0:
            print("Pezhman says: 'Dangerous ⚠️! You're gonna be sick 🤧🤒 and then you're gonna die 💀! "
                  "But don't worry, everybody dies ⚰️, so life is short—enjoy it! 😆'")

        if 0 < self.temperature < 10:
            print("Still too cold for Pezhman 🧥🧣🧤?")

        if 10 < self.temperature < 15:
            print("Hmm, WWPD - what would Pezhman do or wear 🤔? Putting on a vintage barça jersey ⚽️ for sure...")

        if 15 < self.temperature < 20:
            print("Are we approaching Pezhman's comfort zone⁉️")

        if 20 < self.temperature < 35:
            print("I guess Pezhman would like it here 😎, if there is a beach 🏝️🏖️ nearby...?!")

        if self.temperature > 35:
            print("Welcome to hell 🔥 or a very hot place on earth 🥵 or it's just global warming 🌎🌡️.")

    def display_weather_info(self):
        """Print weather details (in our case only temperature) that we got from get_weather function"""
        print(f"\n🌡️ The temperature in {self.city.title()} is: {self.temperature}°C\n")
