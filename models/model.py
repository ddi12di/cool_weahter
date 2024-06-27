from dataclasses import dataclass


@dataclass
class Weather_model:
    temp: int
    feels_like: int
    temp_min: int
    temp_max: int
    pressure: int
    humidity: int
    city: str
    description: str