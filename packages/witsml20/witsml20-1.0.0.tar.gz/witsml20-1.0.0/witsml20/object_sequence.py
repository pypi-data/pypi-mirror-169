from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ObjectSequence:
    """
    Defines a sequence number with an optional description attribute.

    :ivar description: The description of this object sequence.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 2000,
        }
    )
