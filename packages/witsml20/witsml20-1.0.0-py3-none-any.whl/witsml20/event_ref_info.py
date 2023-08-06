from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EventRefInfo:
    """
    Event reference information.

    :ivar event_reference_id: The referencing eventledger ID.
    :ivar event_date: Install/pull date.
    """
    event_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EventReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    event_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EventDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
