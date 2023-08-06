from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.borehole_string import BoreholeString

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BoreholeStringSet:
    """
    Borehole string container element, or a collection of all borehole strings.
    """
    borehole_string: List[BoreholeString] = field(
        default_factory=list,
        metadata={
            "name": "BoreholeString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
