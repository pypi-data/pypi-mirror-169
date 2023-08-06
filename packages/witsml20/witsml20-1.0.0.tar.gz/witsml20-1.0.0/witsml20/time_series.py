from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.geologic_time import GeologicTime
from witsml20.time_series_parentage import TimeSeriesParentage

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimeSeries(AbstractObject):
    """Stores an ordered list of times, for example, for time-dependent
    properties, geometries, or representations.

    It is used in conjunction with the time index to specify times for
    RESQML.

    :ivar time: Individual times composing the series. The list ordering
        is used by the time index.
    :ivar time_series_parentage:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    time: List[GeologicTime] = field(
        default_factory=list,
        metadata={
            "name": "Time",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    time_series_parentage: Optional[TimeSeriesParentage] = field(
        default=None,
        metadata={
            "name": "TimeSeriesParentage",
            "type": "Element",
        }
    )
