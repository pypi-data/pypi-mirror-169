from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_temperature_pressure import AbstractTemperaturePressure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FlowRateValue:
    """
    A possibly temperature and pressure corrected flow rate value.

    :ivar flow_rate: The flow rate of the product. If the 'status'
        attribute is absent and the value is not "NaN", the data value
        can be assumed to be good with no restrictions. A value of "NaN"
        should be interpreted as null and should be not be given unless
        a status is also specified to explain why it is null.
    :ivar measurement_pressure_temperature:
    """
    flow_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    measurement_pressure_temperature: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "MeasurementPressureTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
