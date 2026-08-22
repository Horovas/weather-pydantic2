import json
from urllib.parse import urljoin
import requests

from model_city import WeatherCity


LOG_ENABLED = True
LOG_FILENAME = 'weather_log.txt'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'


def get_weather_city() -> WeatherCity:
    """Gets weather of a certain location"""
    response = requests.get(
        urljoin(BASE_URL, 'forecast'),
        params={
            'id': '50',
            'appid': '123',
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





def write_log(data: list[str]) -> None:
    """Пишем лог в файл."""
    # todo: переписать на logging.info / logging.debug / logging.warning / logging.error
    if not LOG_ENABLED:
        return

    with open(LOG_FILENAME, 'a', encoding='utf-8') as file:
        for line in data:
            file.write(str(line))
        file.write('\n\n')


def main():
    get_weather_city()




main()
