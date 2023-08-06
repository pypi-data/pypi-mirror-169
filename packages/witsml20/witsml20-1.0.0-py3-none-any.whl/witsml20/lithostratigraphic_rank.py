from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LithostratigraphicRank(Enum):
    """
    Specifies the unit of lithostratigraphy.

    :cvar GROUP: A succession of two or more contiguous or associated
        formations with significant and diagnostic lithologic properties
        in common. Formations need not be aggregated into groups unless
        doing so provides a useful means of simplifying stratigraphic
        classification in certain regions or certain intervals.
        Thickness of a stratigraphic succession is not a valid reason
        for defining a unit as a group rather than a formation. The
        component formations of a group need not be everywhere the same.
    :cvar FORMATION: The primary formal unit of lithostratigraphic
        classification. Formations are the only formal
        lithostratigraphic units into which the stratigraphic column
        everywhere should be divided completely on the basis of
        lithology. The contrast in lithology between formations required
        to justify their establishment varies with the complexity of the
        geology of a region and the detail needed for geologic mapping
        and to work out its geologic history. No formation is considered
        justifiable and useful that cannot be delineated at the scale of
        geologic mapping practiced in the region. The thickness of
        formations may range from less than a meter to several thousand
        meters.
    :cvar MEMBER: The formal lithostratigraphic unit next in rank below
        a formation. It possesses lithologic properties distinguishing
        it from adjacent parts of the formation. No fixed standard is
        required for the extent and thickness of a member. A formation
        need not be divided into members unless a useful purpose is thus
        served. Some formations may be completely divided into members;
        others may have only certain parts designated as members. A
        member may extend from one formation to another.
    :cvar BED: The smallest formal unit in the hierarchy of sedimentary
        lithostratigraphic units, e.g. a single stratum lithologically
        distinguishable from other layers above and below. Customarily
        only distinctive beds (key beds, marker beds) particularly
        useful for stratigraphic purposes are given proper names and
        considered formal lithostratigraphic units.
    """
    GROUP = "group"
    FORMATION = "formation"
    MEMBER = "member"
    BED = "bed"
