from pydantic import BaseModel, Field, PositiveInt
from datetime import datetime
from typing import List, Optional


class Coord(BaseModel):
    lat: float
    lon: float


class Main(BaseModel):
    aqi: int


class Components(BaseModel):
    co: float
    no: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float
    nh3: float


class AirPollutionItem(BaseModel):
    main: Main
    components: Components
    dt: datetime


class AirPollutionCoordinates(BaseModel):
    coord: Coord
    air_pollution_list: List[AirPollutionItem] = Field(alias="list")
    model_config = {"populate_by_name": True}


