import json
from urllib.parse import urljoin
import requests


from model_city import WeatherCity
from model_coordinates import WeatherCoordinates
from model_air_pollution_coordinates import AirPollutionCoordinates
from model_geocoding import Geocoding

LOG_ENABLED = True
LOG_FILENAME = 'weather_log.txt'
BASE_URL = 'https://api.openweathermap.org/'
KEY = {
    'key': '123'
}


def get_weather_city() -> WeatherCity:
    """Gets weather of a certain city id"""
    response = requests.get(
        urljoin(BASE_URL, '/data/2.5/forecast'),
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
    """Gets weather at certain coordinates"""
    response = requests.get(
        urljoin(BASE_URL, '/data/2.5/weather'),
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


def get_weather_air_pollution() -> AirPollutionCoordinates:
    """Gets air pollution status of certain coordinates"""
    response = requests.get(
        urljoin(BASE_URL, '/data/2.5/air_pollution'),
        params={
            **KEY,
            'lon': '55.6744',
            'lat': '36.6697',
        }
    )
    response.raise_for_status()

    write_log([
        response.status_code,
        response.url,
        response.text,
    ])

    air_pollution_coordinates = AirPollutionCoordinates.model_validate_json(json_data=response.content)
    print("Air Pollution Coordinates validation complete")
    return air_pollution_coordinates


def get_geocoding() -> Geocoding:
    """Gets geocoding of a certain location"""
    response = requests.get(
        urljoin(BASE_URL, '/geo/1.0/direct'),
        params={
            **KEY,
            'q': 'Rome',
            'limit': '5',
        }
    )
    response.raise_for_status()

    write_log([
        response.status_code,
        response.url,
        response.text,
    ])

    some_geocoding = Geocoding.model_validate_json(json_data=response.content)
    print("Geocoding validation complete")
    return some_geocoding


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
    get_weather_air_pollution()
    get_geocoding()


main()
