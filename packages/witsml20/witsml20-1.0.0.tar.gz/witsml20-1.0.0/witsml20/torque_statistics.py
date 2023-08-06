from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.moment_of_force_measure import MomentOfForceMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TorqueStatistics:
    """
    Measurement of average torque and the channel from which the data was
    calculated.

    :ivar average: Average torque through the interval.
    :ivar channel: Log channel from which the torque statistics were
        calculated.
    """
    average: Optional[MomentOfForceMeasure] = field(
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
