import requests
import datetime
from pprint import pprint
from config import api_key


# Для работы программы надо получить ключ для доступа к API
# в личном кабинете на сайте https://home.openweathermap.org/api_keys

class OpenWeatherMap:
    """ класс для работы с API Openweathermap """

    URL = 'https://api.openweathermap.org/data/2.5/weather?'

    def __init__(self, key):
        self.key = key

    def get_weather(self, city):
        """ возвращает информацию о погоде на день для населенного пункта city """

        data = requests.get(f'{self.URL}q={city}&appid={api_key}&units=metric').json()
        # pprint(data)

        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        city_name = data["name"]
        current_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        return print(f"Дата: {date}\nПогода в городе: {city_name}\nТемпература: {current_weather}°C\n"
                     f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\n"
                     f"Ветер: {wind} м/c")


class CityInfo:

    def __init__(self, city, forecast_provider):
        self.city = city.lower()
        self.forecast_provider = forecast_provider

    def weather_forecast(self):
        return self.forecast_provider.get_weather(self.city)


def main():
    weather_api = OpenWeatherMap(api_key)
    city_name = input("Введите город:")
    city = CityInfo(city_name, weather_api)
    city.weather_forecast()


if __name__ == '__main__':
    main()
