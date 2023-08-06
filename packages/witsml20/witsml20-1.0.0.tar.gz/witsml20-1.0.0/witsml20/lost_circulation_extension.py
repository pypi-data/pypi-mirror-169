from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_event_extension import AbstractEventExtension
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LostCirculationExtension(AbstractEventExtension):
    """
    Information on lost circulation event.

    :ivar volume_lost: Volume lost
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    """
    volume_lost: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeLost",
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
    extension_any: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "ExtensionAny",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
