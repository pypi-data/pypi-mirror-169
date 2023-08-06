from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ReferenceContainer:
    """
    Information on containing or contained components.

    :ivar string_reference_id: DownholeString reference ID.
    :ivar equipment_reference_id: Equipment reference ID.
    :ivar accesory_equipment_reference_id: Reference to the equipment
        for this accessory.
    :ivar comment: Comment or remarks on this container reference.
    :ivar uid: Unique identifier for this instance of
        ReferenceContainer.
    """
    string_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StringReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    equipment_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    accesory_equipment_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccesoryEquipmentReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
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
