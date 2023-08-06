from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_index_value import AbstractIndexValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PassIndexedDepth(AbstractIndexValue):
    """
    Qualifies depth based on pass, direction and depth.

    :ivar pass_value: The pass number. Increase the pass number each
        time the tool direction changes twice.
    :ivar direction: 0 = down (increasing depth) 1= up (decreasing
        depth) Changes each time the logging tool direction changes.
        When a log starts from the bottom, start with pass = 0,
        direction = 1. When you get to the top of the interval and start
        down again, change the pass.
    :ivar depth: The measured depth of the point.
    """
    pass_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    direction: Optional[int] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
