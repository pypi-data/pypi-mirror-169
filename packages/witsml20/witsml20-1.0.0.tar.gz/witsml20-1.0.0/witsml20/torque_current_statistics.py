from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.electric_current_measure import ElectricCurrentMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TorqueCurrentStatistics:
    """
    Measurement of the  average electric current and the channel from which the
    data was calculated.

    :ivar average: Average electric current through the interval
    :ivar channel: Log channel from which the electric current
        statistics were calculated.
    """
    average: Optional[ElectricCurrentMeasure] = field(
        default=None,
        metadata={
            "name": "Average",
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
