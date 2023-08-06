from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_bottom_hole_temperature import AbstractBottomHoleTemperature
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BottomHoleStaticTemperature(AbstractBottomHoleTemperature):
    """
    Static temperature at the bottom of the hole.

    :ivar e_tim_static: Elapsed time since circulation stopped.
    """
    e_tim_static: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "eTimStatic",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
