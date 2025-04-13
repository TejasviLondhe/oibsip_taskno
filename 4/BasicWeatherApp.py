import requests

API_KEY = "6b52f298d80c159dc2b0ac6ca790b286"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Get user input for city
city = input("Enter city name: ").strip()

# Build the API request URL
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    # Fetch data from the API
    response = requests.get(BASE_URL, params=params)
    # print("Raw Response:", response.text)

    response.raise_for_status()  # Check for HTTP errors
    
    # Ensure the response is JSON
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Received invalid JSON from the API.")
        exit()

    # Extract and display weather data
    city_name = data.get('name')
    temperature = data['main'].get('temp')
    humidity = data['main'].get('humidity')
    weather_desc = data['weather'][0].get('description')

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except KeyError:
    print("Error: Unable to fetch weather details. Please check the city name or API key.")
