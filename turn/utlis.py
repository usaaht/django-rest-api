import requests

def get_weather_data(city_name):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=YOUR_API_KEY"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        
        return weather_data
    else:
        
        return None
