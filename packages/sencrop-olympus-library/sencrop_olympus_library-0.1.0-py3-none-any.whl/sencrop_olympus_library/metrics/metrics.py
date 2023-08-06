# Standard Library
from enum import Enum, auto, unique
from typing import Dict, List

# Local
from .units import MetricUnit


class AutoName(Enum):
    # Helper to avoid repeating string values for enums.
    # See https://docs.python.org/3/library/enum.html#using-automatic-values
    def _generate_next_value_(self, start, count, last_values):  # type: ignore
        return self


# TODO: the implementation is a bit weird as we are clearly implementing objects
# Metrics with a name and a unit, as well as other properties like being cumulative


@unique
class Metric(str, AutoName):
    ATMOSPHERIC_PRESSURE_SEA_LEVEL = auto()
    CLOUD_COVER = auto()
    DEW_POINT = auto()
    IRRADIANCE = auto()
    IRRADIANCE_POWER = auto()
    LEAF_WETNESS_HIGH = auto()
    LEAF_WETNESS_LOW = auto()
    LEAF_WETNESS_MEDIUM = auto()
    RAIN_FALL = auto()
    RAIN_PROBABILITY = auto()
    RELATIVE_HUMIDITY = auto()
    TEMPERATURE = auto()
    TEMPERATURE_WMO = auto()
    WET_TEMPERATURE = auto()
    WIND_2M = auto()
    WIND_DIRECTION_10M = auto()
    WIND_DIRECTION_2M = auto()
    WIND_GUST_10M = auto()
    WIND_GUST_2M = auto()
    WIND_SPEED_10M = auto()
    WIND_SPEED_2M = auto()

    def is_cumulative(self) -> bool:
        return self in self.get_cumulative_list()

    @staticmethod
    def get_cumulative_list() -> List["Metric"]:
        return [
            Metric.LEAF_WETNESS_HIGH,
            Metric.LEAF_WETNESS_LOW,
            Metric.LEAF_WETNESS_MEDIUM,
            Metric.IRRADIANCE,
            Metric.IRRADIANCE_POWER,
            Metric.RAIN_FALL,
        ]


DEFAULT_UNITS: Dict[Metric, MetricUnit] = {
    Metric.ATMOSPHERIC_PRESSURE_SEA_LEVEL: MetricUnit.HECTO_PASCAL,
    Metric.CLOUD_COVER: MetricUnit.PERCENTAGE,
    Metric.DEW_POINT: MetricUnit.CELSIUS,
    Metric.IRRADIANCE: MetricUnit.MEGA_JOULE_PER_SQUARE_METER,
    Metric.IRRADIANCE_POWER: MetricUnit.WATT_PER_SQUARE_METER,
    Metric.LEAF_WETNESS_HIGH: MetricUnit.TIME_IN_MINUTES,
    Metric.LEAF_WETNESS_LOW: MetricUnit.TIME_IN_MINUTES,
    Metric.LEAF_WETNESS_MEDIUM: MetricUnit.TIME_IN_MINUTES,
    Metric.RAIN_FALL: MetricUnit.MILLIMETER,
    Metric.RAIN_PROBABILITY: MetricUnit.PERCENTAGE,
    Metric.RELATIVE_HUMIDITY: MetricUnit.PERCENTAGE,
    Metric.TEMPERATURE: MetricUnit.CELSIUS,
    Metric.TEMPERATURE_WMO: MetricUnit.CELSIUS,
    Metric.WET_TEMPERATURE: MetricUnit.CELSIUS,
    Metric.WIND_2M: MetricUnit.KILOMETER_PER_HOUR,
    Metric.WIND_DIRECTION_10M: MetricUnit.DEGREES,
    Metric.WIND_DIRECTION_2M: MetricUnit.DEGREES,
    Metric.WIND_GUST_10M: MetricUnit.KILOMETER_PER_HOUR,
    Metric.WIND_GUST_2M: MetricUnit.KILOMETER_PER_HOUR,
    Metric.WIND_SPEED_10M: MetricUnit.KILOMETER_PER_HOUR,
    Metric.WIND_SPEED_2M: MetricUnit.KILOMETER_PER_HOUR,
}
