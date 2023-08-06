from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.event_class_type import EventTypeType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EventType:
    """
    The type of the referencing event.

    :ivar value:
    :ivar class_value: The type of the event (job, daily report, etc.)
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    class_value: Optional[EventTypeType] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
            "required": True,
        }
    )
