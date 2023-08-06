from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.perforation_set import PerforationSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforationSets:
    """
    Information on the collection of perforation sets.
    """
    perforation_set: List[PerforationSet] = field(
        default_factory=list,
        metadata={
            "name": "PerforationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
