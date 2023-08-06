from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.borehole_string_reference import BoreholeStringReference
from witsml20.downhole_string_reference import DownholeStringReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeComponentReference:
    """
    Reference to a downhole component identifier.

    :ivar string_equipment_reference_id: Reference to string equipment
    :ivar perforation_set_reference_id: Reference to perforation set
    :ivar borehole_string_reference:
    :ivar downhole_strings_reference:
    """
    string_equipment_reference_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StringEquipmentReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    perforation_set_reference_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PerforationSetReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    borehole_string_reference: List[BoreholeStringReference] = field(
        default_factory=list,
        metadata={
            "name": "BoreholeStringReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    downhole_strings_reference: List[DownholeStringReference] = field(
        default_factory=list,
        metadata={
            "name": "DownholeStringsReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
