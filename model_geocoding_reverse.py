from pydantic import BaseModel, Field, TypeAdapter, RootModel, PositiveInt
from typing import Dict, List, Optional


class City(BaseModel):
    name: str
    local_names: Optional[Dict[str, str]] = Field(default=None)
    lat: float
    lon: float
    country: str
    state: str


class GeocodingReverse(RootModel[List[City]]):
    pass




