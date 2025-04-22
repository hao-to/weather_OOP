from weather_OOP import WeatherApp
from db import init_db, save_to_db, export_to_csv

print("\nWelcome to the WeatherApp ⛅️🌤️⛈️!\n☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️\n")
init_db()  # ensure the DB exists

city = input("Enter the name of the city: ").strip()

# Create WeatherApp instance with user's input
app = WeatherApp(city)

# Get coordinates (with using API Ninjas)
app.get_coordinates()

# Exit early, if coordinates couldn't be retrieved
if app.lat is None or app.lon is None:
    print("Could not retrieve coordinates. Exiting program.")
    exit()

# Menu loop
while True:
    print("\n--- WeatherApp Menu ---")
    print("1. Show Current Weather🌤️")
    print(f"2. Hear what Pezhman says about the weather in {city.title()} 😁🧔🏻‍")
    print("3. Display Coordinates 🌎")
    print("4. Save current weather to database 🗃️")
    print("5. Export all saved data to CSV 📄")
    print("6. Show 7-Day Forecast 📅")
    print("7. Get clothing advice from OpenAI 🤖")
    print("8. Exit")

    choice = input("Select an option (1–8): ").strip()

    if choice == "1":
        app.get_weather()
        app.display_weather_info()
    elif choice == "2":
        app.pezhman_says()
    elif choice == "3":
        print(f"\nCoordinates for {city.title()}:\n- Latitude: {app.lat}\n- Longitude: {app.lon}")
    elif choice == "4":
        app.get_weather()  # make sure temperature is fresh
        if app.lat and app.lon and app.temperature is not None:
            save_to_db(city, app.temperature, app.lat, app.lon)
            print("✅ Weather data saved to database.")
        else:
            print("⚠️ Cannot save – missing information.")

    elif choice == "5":
        export_to_csv()
        print("✅ Data exported to 'weather_history.csv'.")
    elif choice == "6":
        app.show_7_day_forecast()

    elif choice == "7":
        app.ask_openai_clothing()

    elif choice == "8":
        print("\nExiting WeatherApp. Goodbye!")
        break

