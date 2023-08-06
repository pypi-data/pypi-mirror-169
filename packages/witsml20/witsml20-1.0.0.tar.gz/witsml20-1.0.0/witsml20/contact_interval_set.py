from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.gravel_pack_interval import GravelPackInterval
from witsml20.open_hole_interval import OpenHoleInterval
from witsml20.perforation_set_interval import PerforationSetInterval
from witsml20.slots_interval import SlotsInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ContactIntervalSet:
    """Information on a collection of contact intervals.

    Contains one or more "xxxInterval" objects, each representing the
    details of a single physical connection between well and reservoir,
    e.g., the perforation details, depth, reservoir connected. Meaning:
    this is the physical nature of a connection from reservoir to
    wellbore.
    """
    slots_interval: List[SlotsInterval] = field(
        default_factory=list,
        metadata={
            "name": "SlotsInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    open_hole_interval: List[OpenHoleInterval] = field(
        default_factory=list,
        metadata={
            "name": "OpenHoleInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set_interval: List[PerforationSetInterval] = field(
        default_factory=list,
        metadata={
            "name": "PerforationSetInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gravel_pack_interval: List[GravelPackInterval] = field(
        default_factory=list,
        metadata={
            "name": "GravelPackInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
