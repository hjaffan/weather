import requests
import os

api_key = os.getenv('API_KEY','')

#TODO: Convert defaults to config file
def getWeatherRequest(url="api.openweathermap.org/data/2.5/weather", cityid="5344994"):
    full_url = "https://{}?id={}&APPID={}".format(url, cityid, api_key)
    response = requests.get(full_url)

    if response.status_code != 200:
        print("Site returned a non valid response")
    return response.json()


def getWeather():
    response = getWeatherRequest(cityid="5344994")
    degree_in_kelvin = response['main']['temp']
    celcius = float(degree_in_kelvin) - float(273.15)
    fahrenheit = (float(degree_in_kelvin) - 273.15) * 9/5 + 32
    print("The Weather in LA is: {} C and {} F".format(round(celcius, 2), round(fahrenheit, 2)))


if __name__ == "__main__":
    getWeather()