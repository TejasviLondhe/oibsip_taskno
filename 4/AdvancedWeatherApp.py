import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

API_KEY = "6b52f298d80c159dc2b0ac6ca790b286"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather():
    city = city_entry.text().strip()
    if not city:
        QMessageBox.critical(window, "Error", "Please enter a city name!")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract weather details
        city_name = data.get('name')
        temperature = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        weather_desc = data['weather'][0].get('description').capitalize()

        result_label.setText(f"Weather in {city_name}:")
        temp_label.setText(f"Temperature: {temperature}°C")
        humidity_label.setText(f"Humidity: {humidity}%")
        desc_label.setText(f"Condition: {weather_desc}")

    except requests.exceptions.RequestException as e:
        QMessageBox.critical(window, "Error", f"Request failed: {e}")
    except KeyError:
        QMessageBox.critical(window, "Error", "Unable to fetch weather details. Check city name or API key.")

# GUI setup
app = QApplication([])
window = QWidget()
window.setWindowTitle("Weather App")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()

# Input field
city_entry = QLineEdit()
city_entry.setPlaceholderText("Enter city name")
layout.addWidget(city_entry)

# Fetch button
fetch_button = QPushButton("Get Weather")
fetch_button.clicked.connect(get_weather)
layout.addWidget(fetch_button)

# Result labels
result_label = QLabel("")
temp_label = QLabel("")
humidity_label = QLabel("")
desc_label = QLabel("")

layout.addWidget(result_label)
layout.addWidget(temp_label)
layout.addWidget(humidity_label)
layout.addWidget(desc_label)

window.setLayout(layout)
window.show()
app.exec_()
