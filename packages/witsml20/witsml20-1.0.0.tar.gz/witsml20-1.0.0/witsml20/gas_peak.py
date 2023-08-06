from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.gas_peak_type import GasPeakType
from witsml20.length_measure import LengthMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GasPeak:
    """
    Readings at maximum gas production.

    :ivar peak_type: Type of gas peak
    :ivar md_peak: Measured depth at which the gas reading was taken.
    :ivar average_gas: Average total gas.
    :ivar peak_gas: Peak gas reading.
    :ivar background_gas: Background gas reading.
    :ivar channel:
    """
    peak_type: Optional[GasPeakType] = field(
        default=None,
        metadata={
            "name": "PeakType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    md_peak: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdPeak",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_gas: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AverageGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    peak_gas: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PeakGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    background_gas: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BackgroundGas",
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
            "required": True,
        }
    )
