from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_index_value import AbstractIndexValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthIndexValue(AbstractIndexValue):
    """
    Qualifies the index as depth.

    :ivar depth: Used to specify the channel start and end index.
    """
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
