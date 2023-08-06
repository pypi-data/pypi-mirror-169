from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_iscwsa_error_coefficient import AbstractIscwsaErrorCoefficient

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Depth(AbstractIscwsaErrorCoefficient):
    """
    Describes what survey measurement or value the error term applies to.

    :ivar depth: The measured depth of the point.
    """
    depth: Optional[str] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
