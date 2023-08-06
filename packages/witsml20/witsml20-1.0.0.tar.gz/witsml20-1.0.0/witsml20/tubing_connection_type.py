from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_connection_type import AbstractConnectionType
from witsml20.tubing_connection_types import TubingConnectionTypes

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubingConnectionType(AbstractConnectionType):
    """
    Container element for tubing connection types  or collection of tubing
    connection types.

    :ivar tubing_connection_type: Tubing connection type.
    """
    tubing_connection_type: Optional[TubingConnectionTypes] = field(
        default=None,
        metadata={
            "name": "TubingConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
