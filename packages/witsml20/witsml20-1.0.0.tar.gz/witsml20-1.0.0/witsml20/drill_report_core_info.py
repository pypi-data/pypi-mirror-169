from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.inner_barrel_type import InnerBarrelType
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.tvd_interval import TvdInterval
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportCoreInfo:
    """
    General information about a core taken during the drill report period.

    :ivar dtim: Date and time that the core was completed.
    :ivar core_number: Core identification number.
    :ivar cored_md_interval: Cored interval expressed as measured depth.
    :ivar cored_tvd_interval: Cored interval expressed as true vertical
        depth.
    :ivar len_recovered: Length of the core recovered.
    :ivar recover_pc: The relative amount of core recovered.
    :ivar len_barrel: Length of  the core barrel.
    :ivar inner_barrel_type: Core inner barrel type.
    :ivar core_description: General core description.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportCoreInfo.
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
    core_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoreNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cored_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "CoredMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cored_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "CoredTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_recovered: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenRecovered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    recover_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RecoverPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_barrel: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenBarrel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    inner_barrel_type: Optional[InnerBarrelType] = field(
        default=None,
        metadata={
            "name": "InnerBarrelType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    core_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoreDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
