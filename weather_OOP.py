import requests
from dotenv import load_dotenv
import os
from openai import OpenAI


# Load .env file
load_dotenv()

# Retrieve API key
API_KEY = os.getenv("API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


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

    def pezhman_says(self):
        """Prints Pezhman's weather-based comments."""
        if self.temperature is None:
            self.get_weather()

        if self.temperature < 0:
            print(f"\nPezhman says: 'Only {self.temperature}°C?! F**king freezzzyyy! Stay at home! 🥶'")

        elif 0 <= self.temperature < 10:
            print(f"\nPezhman says: 'It's only {self.temperature}°C. Dangerous to go outside ⚠️! "
                  f"You're gonna be sick 🤧🤒 and then you're gonna die 💀! "
                  "But don't worry, everybody dies ⚰️, so life is short—enjoy it! 😆'")

        elif 10 <= self.temperature < 15:
            print(f"\nWith {self.temperature}°C it's still too cold for Pezhman 🧥🧣🧤?")

        elif 15 <= self.temperature < 20:
            print(f"\nHmm, we have {self.temperature}°C now. WWPD - "
                  f"what would Pezhman do or wear 🤔? Putting on a vintage barça jersey ⚽️ for sure...")

        elif 20 <= self.temperature < 25:
            print(f"\nAre we approaching Pezhman's comfort zone with {self.temperature}°C⁉️")

        elif 25 <= self.temperature < 35:
            print(f"\nI guess Pezhman would like it here 😎 with {self.temperature}°C, "
                  f"if there is a beach 🏝️🏖️ nearby...?!")

        else:
            print("\nWelcome to hell 🔥 or a very hot place on earth 🥵 or it's just global warming 🌎🌡️.")

    def display_weather_info(self):
        """Print weather details (in our case only temperature) that we got from get_weather function"""
        print(f"\n🌡️ The temperature in {self.city.title()} is: {self.temperature}°C\n")

    def show_7_day_forecast(self):
        """Fetches 7-day weather forecast using Open-Meteo API."""
        if self.lat is None or self.lon is None:
            print("Error: Cannot get forecast without coordinates.")
            return

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            dates = data["daily"]["time"]
            temps_max = data["daily"]["temperature_2m_max"]
            temps_min = data["daily"]["temperature_2m_min"]

            print(f"\n📅 7-Day Forecast for {self.city.title()}:\n")
            for date, t_min, t_max in zip(dates, temps_min, temps_max):
                print(f"{date}: Min. Temperature is: {t_min}°C – Max. Temperature is: {t_max}°C")
        else:
            print("Error: Could not retrieve forecast data.")

    def ask_openai_clothing(self):
        """Ask OpenAI for clothing suggestion based on temperature."""
        if self.temperature is None:
            self.get_weather()

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        messages = [
            {"role": "system", "content": "You are a funny, sarcastic and maybe helpful clothing assistant."},
            {"role": "user", "content": f"It's {self.temperature}°C. I'm a complete moron and can't think for myself. "
                                        f"Tell me what to wear or do today!"}
        ]

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            print(f"\n🤖 OpenAI says:\n{response.choices[0].message.content}\n")
        except Exception as e:
            print(f"⚠️ Error fetching OpenAI response: {e}")


