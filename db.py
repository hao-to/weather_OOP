import sqlite3
import csv

def init_db():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            latitude REAL,
            longitude REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(city, temperature, lat, lon):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_history (city, temperature, latitude, longitude)
        VALUES (?, ?, ?, ?)
    ''', (city.title(), temperature, lat, lon))
    conn.commit()
    conn.close()

def export_to_csv():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT city, temperature, latitude, longitude FROM weather_history")
    data = cursor.fetchall()
    conn.close()

    with open("weather_history.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["City", "Temperature", "Latitude", "Longitude"])
        writer.writerows(data)
