from pydantic import BaseModel, Field, PositiveInt
from datetime import datetime
from typing import List, Optional


class Sys(BaseModel):
    country: str
    sunrise: datetime
    sunset: datetime


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class MainWeatherData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class WeatherInfo(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Coord(BaseModel):
    lat: float
    lon: float


class WeatherCoordinates(BaseModel):
    coord: Coord
    weather: List[WeatherInfo]
    base: str
    main: MainWeatherData
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: datetime
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int




