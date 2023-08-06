from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_connection_type import AbstractConnectionType
from witsml20.other_connection_types import OtherConnectionTypes

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class OtherConnectionType(AbstractConnectionType):
    """
    Allows you to enter a connection type other than the ones in the standard
    list.

    :ivar other_connection_type: Connection type other than rod, casing
        or tubing.
    """
    other_connection_type: Optional[OtherConnectionTypes] = field(
        default=None,
        metadata={
            "name": "OtherConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
