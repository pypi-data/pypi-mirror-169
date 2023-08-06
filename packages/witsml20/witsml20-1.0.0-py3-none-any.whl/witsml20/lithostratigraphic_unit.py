from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.lithostratigraphic_rank import LithostratigraphicRank

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LithostratigraphicUnit:
    """The name of a lithostratigraphy, with the "kind" attribute specifying
    the lithostratigraphic unit-hierarchy (group, formation, member or bed).

    The entry at each level is free text for the local lithostratigraphy
    at that level in the hierarchy. If a single hierarchy is defined, it
    is assumed this is at the formation level in the hierarchy and
    kind=formation should be used for the entry. Used to hold
    information about the stratigraphic units that an interpreted
    lithology may belong to. These are based primarily on the
    differences between rock types rather than their specific age. For
    example, in the Grand Canyon, some of the major lithostratigraphic
    units are the "Navajo", "Kayenta", "Wingate", "Chinle" and
    "Moenkopi" formations, each of which is represented by a particular
    set of rock properties or characteristics.

    :ivar value:
    :ivar authority: Person or collective body responsible for
        authorizing the information.
    :ivar kind: Specifies the lithostratigraphic unit-hierarchy (group,
        formation, member or bed).
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    kind: Optional[LithostratigraphicRank] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
