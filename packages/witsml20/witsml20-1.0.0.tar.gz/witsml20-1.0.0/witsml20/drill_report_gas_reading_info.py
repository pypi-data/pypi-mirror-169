from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.gas_peak_type import GasPeakType
from witsml20.md_interval import MdInterval
from witsml20.tvd_interval import TvdInterval
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportGasReadingInfo:
    """
    General information about a gas reading taken during the drill report
    period.

    :ivar dtim: Date and time of the gas reading.
    :ivar reading_type: Type of gas reading.
    :ivar gas_reading_md_interval: Measured depth interval over which
        the gas reading was conducted.
    :ivar gas_reading_tvd_interval: True vertical depth interval over
        which the gas reading was conducted.
    :ivar gas_high: The highest gas reading.
    :ivar gas_low: The lowest gas reading.
    :ivar meth: Methane (C1) concentration.
    :ivar eth: Ethane (C2) concentration.
    :ivar prop: Propane (C3) concentration.
    :ivar ibut: Iso-butane (iC4) concentration.
    :ivar nbut: Nor-butane (nC4) concentration.
    :ivar ipent: Iso-pentane (iC5) concentration.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportGasReadingInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    reading_type: Optional[GasPeakType] = field(
        default=None,
        metadata={
            "name": "ReadingType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_reading_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "GasReadingMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_reading_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "GasReadingTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_high: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasHigh",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_low: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasLow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    meth: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Meth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    eth: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Eth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    prop: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Prop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ibut: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Ibut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nbut: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Nbut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ipent: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Ipent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
