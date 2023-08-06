from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractIscwsaErrorCoefficient:
    """
    Describes the survey measurement or value that the error term applies to.

    :ivar uid: Unique identifier for this instance of
        AbstractIscwsaErrorCoefficient.
    """
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
