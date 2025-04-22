# Weather OOP App ☁️🌡️

A simple weather app built in Python using object-oriented programming.  
Users can enter a city name and interact with a small terminal menu to:

- 🌍 Get the current weather  
- 🧭 View geographic coordinates  
- 🧥 Hear what Pezhman says about the weather (with a sense of humor)
- 📅 See the 7-day forecast 
- 💾 Save weather data to a database
- 📤 Export saved weather history to a CSV file
- 🤖 Optional: Get clothing advice from OpenAI (requires your own API key)


---

## 💡 About this Project

This app was created during a software engineering bootcamp as a practice exercise using APIs, user input, and OOP principles.

It uses:
- [API Ninjas Geocoding API](https://api-ninjas.com/api/geocoding) to get latitude and longitude  
- [Open-Meteo API](https://open-meteo.com/) for current weather data

Yes – it’s a very basic app.  
Sad, I know. But somehow fitting — since *Pezhman* literally means “sad” in Farsi,  
and is also a name — the name of the tutor who gave me this assignment 😄  
...and who also happens to be a huge fan of FC Barcelona ⚽ and warm weather ☀️😎  
I’m still learning — and this is just the beginning. 💻✨

---

## 🛠 How to Run

1. Clone this repository  
2. Create a `.env` file in the root folder:

```env
API_KEY=your_api_ninjas_key_here
```

3. (Optional) Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

4. Run `main.py` in your terminal or via your IDE (e.g. PyCharm)

---

## ✨ Features

- OOP design in Python  
- Terminal-based user menu  
- Integration with two external APIs  
- Basic error handling  
- A tiny bit of personality 🧠🎭

---

## 🗺️ Next Steps (Maybe)

- Add weather forecast for the next few days  
- Switch between Celsius and Fahrenheit  
- Maybe even build a GUI version one day

## ⚠️ Important Notice about OpenAI API Usage

This project includes an optional feature to get clothing advice from OpenAI's GPT model.  
To use it, you must:

- Create an OpenAI account at [https://platform.openai.com/signup](https://platform.openai.com/signup)
- Add a valid payment method
- Generate an API key and save it in your `.env` file as:

```env
OPENAI_API_KEY=your_openai_key_here
```
