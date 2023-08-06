from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_connection_type import AbstractConnectionType
from witsml20.casing_connection_types import CasingConnectionTypes

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CasingConnectionType(AbstractConnectionType):
    """
    Container element for casing connections or collection of all casing
    connections information.

    :ivar casing_connection_type: Connection of type casing.
    """
    casing_connection_type: Optional[CasingConnectionTypes] = field(
        default=None,
        metadata={
            "name": "CasingConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
