# Standard Library
from enum import Enum


class MetricUnit(str, Enum):
    CELSIUS = "°C"
    DEGREES = "°"
    HECTO_PASCAL = "hPa"
    KILOMETER_PER_HOUR = "km/h"
    MEGA_JOULE_PER_SQUARE_METER = "MJ/m2"
    MILLIMETER = "mm"
    PERCENTAGE = "%"
    TIME_IN_MINUTES = "mn"
    WATT_PER_SQUARE_METER = "W/m2"
