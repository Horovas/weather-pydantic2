import json
from urllib.parse import urljoin
import requests

from model_city import WeatherCity
from model_coordinates import WeatherCoordinates


LOG_ENABLED = True
LOG_FILENAME = 'weather_log.txt'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'
KEY = {
    'key': '123'
}


def get_weather_city() -> WeatherCity:
    """Gets weather of a certain city id"""
    response = requests.get(
        urljoin(BASE_URL, 'forecast'),
        params={
            **KEY,
            'id': '498817',
        }
    )
    response.raise_for_status()

    write_log([
        response.status_code,
        response.url,
        response.text,
    ])

    weather_city = WeatherCity.model_validate_json(json_data=response.content)
    print("Weather City validation complete")
    return weather_city


def get_weather_coordinates() -> WeatherCoordinates:
    """Gets weather of a certain coordinates"""
    response = requests.get(
        urljoin(BASE_URL, 'weather'),
        params={
            **KEY,
            'lon': '48',
            'lat': '30',
        }
    )
    response.raise_for_status()

    write_log([
        response.status_code,
        response.url,
        response.text,
    ])

    weather_coordinates = WeatherCoordinates.model_validate_json(json_data=response.content)
    print("Weather Coordinates validation complete")
    return weather_coordinates


def write_log(data: list[str]) -> None:
    """Adding log to a file"""
    if not LOG_ENABLED:
        return

    with open(LOG_FILENAME, 'a', encoding='utf-8') as file:
        for line in data:
            file.write(str(line))
            file.write('  ')
        file.write('\n\n')


def main():
    get_weather_city()
    get_weather_coordinates()


main()
