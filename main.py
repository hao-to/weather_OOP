from weather_OOP import WeatherApp
print("\nWelcome to the WeatherApp ⛅️🌤️⛈️!\n☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️\n")

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
    print("2. Hear what Pezhman says about the weather 😁🧔🏻‍")
    print("3. Display Coordinates 🌎")
    print("4. Exit")

    choice = input("Select an option (1–4): ").strip()

    if choice == "1":
        app.get_weather()
        app.display_weather_info()
    elif choice == "2":
        app.pezhman_says()
    elif choice == "3":
        print(f"\nCoordinates for {city.title()}:\n- Latitude: {app.lat}\n- Longitude: {app.lon}")
    elif choice == "4":
        print("\nExiting WeatherApp. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

