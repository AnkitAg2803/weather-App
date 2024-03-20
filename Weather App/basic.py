import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = 'd17a221d2c977b6f8a6c452ac68470c9'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'].title(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather
    else:
        return None

def fetch_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        messagebox.showinfo('Weather', f"Weather: {weather['description']}\nTemperature: {weather['temperature']}°C\nHumidity: {weather['humidity']}%\nWind Speed: {weather['wind_speed']} m/s")
    else:
        messagebox.showerror('Error', 'City not found.')

# GUI setup
root = tk.Tk()
root.title('Weather App')
root.geometry("400x300") 

city_label = tk.Label(root, text='Enter city:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text='Fetch Weather', command=fetch_weather)
fetch_button.pack()

root.mainloop()
