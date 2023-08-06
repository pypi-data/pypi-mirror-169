from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.length_per_time_measure import LengthPerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RopStatistics:
    """
    Measurements on minimum, average and maximum rates of penetration (ROP) and
    the channel from which this data was calculated.

    :ivar average: Average rate of penetration through the interval.
    :ivar minimum: Minimum rate of penetration through the interval.
    :ivar maximum: Maximum rate of penetration through the interval.
    :ivar channel: Log channel from which the ROP statistics were
        calculated.
    """
    average: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "Average",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    minimum: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    maximum: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
