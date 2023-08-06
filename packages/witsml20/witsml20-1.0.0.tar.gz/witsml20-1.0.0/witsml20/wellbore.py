from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.time_measure import TimeMeasure
from witsml20.well_purpose import WellPurpose
from witsml20.well_status import WellStatus
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord
from witsml20.wellbore_shape import WellboreShape
from witsml20.wellbore_type import WellboreType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Wellbore(AbstractObject):
    """Used to capture the general information about a wellbore.

    This information is sometimes called a "wellbore header". A wellbore
    represents the path from surface to a unique bottomhole location.
    The wellbore object is uniquely identified within the context of one
    well object.

    :ivar number: Operator borehole number.
    :ivar suffix_api: API suffix.
    :ivar num_govt: Government assigned number.
    :ivar status_wellbore: POSC wellbore status.
    :ivar is_active: True (="1" or "true") indicates that the wellbore
        is active. False (="0" or "false") indicates otherwise. It is
        the servers responsibility to set this value based on its
        available internal data (e.g., what objects are changing).
    :ivar purpose_wellbore: POSC wellbore purpose.
    :ivar type_wellbore: Type of wellbore.
    :ivar shape: POSC wellbore trajectory shape.
    :ivar dtim_kickoff: Date and time of wellbore kickoff.
    :ivar achieved_td: True ("true" of "1") indicates that the wellbore
        has acheieved total depth. That is, drilling has completed.
        False ("false" or "0") indicates otherwise. Not given indicates
        that it is not known whether total depth has been reached.
    :ivar md: The measured depth of the borehole. If status is plugged,
        indicates the maximum depth reached before plugging. It is
        recommended that this value be updated about every 10 minutes by
        an assigned raw data provider at a site.
    :ivar tvd: The  true vertical depth of the borehole. If status is
        plugged, indicates the maximum depth reached before plugging. It
        is recommended that this value be updated about every 10 minutes
        by an assigned raw data provider at a site.
    :ivar md_bit: The measured depth of the bit. If isActive=false then
        this value is not relevant. It is recommended that this value be
        updated about every 10 minutes by an assigned raw data provider
        at a site.
    :ivar tvd_bit: The true vertical depth of the bit. If isActive=false
        then this value is not relevant. It is recommended that this
        value be updated about every 10 minutes by an assigned raw data
        provider at a site.
    :ivar md_kickoff: Kickoff measured depth of the wellbore.
    :ivar tvd_kickoff: Kickoff true vertical depth of the wellbore.
    :ivar md_planned: Planned measured depth for the wellbore total
        depth.
    :ivar tvd_planned: Planned true vertical depth for the wellbore
        total depth.
    :ivar md_sub_sea_planned: Planned measured for the wellbore total
        depth - with respect to seabed.
    :ivar tvd_sub_sea_planned: Planned true vertical depth for the
        wellbore total depth - with respect to seabed.
    :ivar day_target: Target days for drilling wellbore.
    :ivar well:
    :ivar parent_wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "max_length": 64,
        }
    )
    suffix_api: Optional[str] = field(
        default=None,
        metadata={
            "name": "SuffixAPI",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_govt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumGovt",
            "type": "Element",
            "max_length": 64,
        }
    )
    status_wellbore: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "StatusWellbore",
            "type": "Element",
        }
    )
    is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        }
    )
    purpose_wellbore: Optional[WellPurpose] = field(
        default=None,
        metadata={
            "name": "PurposeWellbore",
            "type": "Element",
        }
    )
    type_wellbore: Optional[WellboreType] = field(
        default=None,
        metadata={
            "name": "TypeWellbore",
            "type": "Element",
        }
    )
    shape: Optional[WellboreShape] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    dtim_kickoff: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimKickoff",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    achieved_td: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AchievedTD",
            "type": "Element",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
        }
    )
    md_bit: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdBit",
            "type": "Element",
        }
    )
    tvd_bit: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdBit",
            "type": "Element",
        }
    )
    md_kickoff: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdKickoff",
            "type": "Element",
        }
    )
    tvd_kickoff: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdKickoff",
            "type": "Element",
        }
    )
    md_planned: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdPlanned",
            "type": "Element",
        }
    )
    tvd_planned: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdPlanned",
            "type": "Element",
        }
    )
    md_sub_sea_planned: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdSubSeaPlanned",
            "type": "Element",
        }
    )
    tvd_sub_sea_planned: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdSubSeaPlanned",
            "type": "Element",
        }
    )
    day_target: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "DayTarget",
            "type": "Element",
        }
    )
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "required": True,
        }
    )
    parent_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentWellbore",
            "type": "Element",
        }
    )
