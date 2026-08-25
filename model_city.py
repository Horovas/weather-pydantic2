from pydantic import BaseModel, Field, PositiveInt
from datetime import datetime
from typing import List, Optional


class Sys(BaseModel):
    pod: str


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Clouds(BaseModel):
    all: int


class WeatherInfo(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainWeatherData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float
    dew_point: float


class ForecastItem(BaseModel):
    dt: datetime
    main: MainWeatherData
    weather: List[WeatherInfo]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: float
    sys: Sys
    dt_txt: str
    

class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str
    coord: Coord
    country: str
    population: int
    timezone: int
    sunrise: datetime
    sunset: datetime


class WeatherCity(BaseModel):
    cod: str
    message: int
    cnt: int
    forecast_list: List[ForecastItem] = Field(alias="list")
    city: City
    model_config = {"populate_by_name": True}


