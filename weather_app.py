import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "089b25efc86bd14100d4c210fb78ec0f"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Enter City Name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        
        print(data)
        if data["cod"] != 200:
            messagebox.showerror("Error", "City Not Found")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]

        result.config(
            text=f"""
City : {city_name}, {country}

🌡 Temperature : {temp} °C

☁ Weather : {weather}

💧 Humidity : {humidity} %

🌬 Wind Speed : {wind} m/s

🧭 Pressure : {pressure} hPa
""",
            fg="white"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("500x500")
root.config(bg="#1E3A5F")

title = tk.Label(
    root,
    text="🌤 Weather Forecast",
    font=("Arial", 22, "bold"),
    bg="#1E3A5F",
    fg="white"
)
title.pack(pady=20)

city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    justify="center"
)
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Search",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    command=get_weather
)
search_btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#1E3A5F",
    justify="left"
)
result.pack(pady=30)

root.mainloop()