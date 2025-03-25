from weather_OOP import WeatherApp

# ask the user for a city name
city = input("Enter the name of the city: ").strip()

# create WeatherApp object with user input
app = WeatherApp(city)

# get coordinates (with possible multiple matches)
app.get_coordinates()
print(f"\nHere is the geo data for your city: {city.title()}\n- Latitude: {app.lat}\n- Longitude: {app.lon}")


app.get_weather()

app.display_weather_info()

app.suggest_clothing()
