from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerfSlot:
    """
    Information on slot resulting from a perforation.

    :ivar slot_height: The height of slot.
    :ivar slot_width: The width of the slot.
    :ivar slot_center_distance: Distance from center point.
    :ivar slot_count: The number of the slots.
    :ivar remarks: Remarks and comments about this perforation slot.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of PerfSlot.
    """
    slot_height: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SlotHeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slot_width: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SlotWidth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slot_center_distance: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SlotCenterDistance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slot_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remarks",
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
