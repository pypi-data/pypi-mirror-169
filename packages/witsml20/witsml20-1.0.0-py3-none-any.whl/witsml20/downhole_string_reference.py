from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeStringReference:
    """
    Refernce to a downhole string identifier.

    :ivar string_equipment_reference_id: Reference to string equipment
    :ivar downhole_string_reference_id: Reference to downhole string
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
    downhole_string_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "downholeStringReferenceId",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
