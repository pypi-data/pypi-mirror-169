from __future__ import annotations
from dataclasses import dataclass
from witsml20.abstract_bottom_hole_temperature import AbstractBottomHoleTemperature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BottomHoleCirculatingTemperature(AbstractBottomHoleTemperature):
    """
    Circulating temperature at the bottom of the hole.
    """
