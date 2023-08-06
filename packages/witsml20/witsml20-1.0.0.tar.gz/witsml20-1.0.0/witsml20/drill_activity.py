from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.drill_activity_class_type import DrillActivityTypeType
from witsml20.drill_activity_code import DrillActivityCode
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.item_state import ItemState
from witsml20.md_interval import MdInterval
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.object_alias import ObjectAlias
from witsml20.state_detail_activity import StateDetailActivity
from witsml20.time_measure import TimeMeasure
from witsml20.tvd_interval import TvdInterval
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillActivity:
    """
    Operations Activity Component Schema.

    :ivar dtim_start: Date and time that activities started.
    :ivar dtim_end: Date and time that activities ended.
    :ivar duration: The activity duration (commonly in hours).
    :ivar md: The measured depth to the drilling activity/operation.
    :ivar tvd: True vertical depth to the drilling activity/operation.
    :ivar phase: Phase refers to a large activity classification, e.g.,
        drill surface hole.
    :ivar activity_code: A code used to define rig activity.
    :ivar detail_activity: Custom string to further define an activity.
    :ivar type_activity_class: Classifier (planned, unplanned,
        downtime).
    :ivar activity_md_interval: Measured depth interval over which the
        activity was conducted.
    :ivar activity_tvd_interval: True vertical depth interval over which
        the activity was conducted.
    :ivar bit_md_interval: Range of bit measured depths over which the
        activity occurred.
    :ivar state: Finish, interrupted, failed, etc.
    :ivar state_detail_activity: The outcome of the detailed activity.
    :ivar operator: Operator company name.
    :ivar tubular: A pointer to the tubular object  related to this
        activity.
    :ivar optimum: Is the activity optimum.? Values are "true" (or "1")
        and "false" (or "0").
    :ivar productive: Does activity bring closer to objective?  Values
        are "true" (or "1") and "false" (or "0").
    :ivar item_state: The item state for the data object.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar proprietary_code:
    :ivar uid: Unique identifier for this instance of DrillActivity.
    """
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    activity_code: Optional[DrillActivityCode] = field(
        default=None,
        metadata={
            "name": "ActivityCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    detail_activity: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type_activity_class: Optional[DrillActivityTypeType] = field(
        default=None,
        metadata={
            "name": "TypeActivityClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    activity_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "ActivityMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    activity_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "ActivityTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bit_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "BitMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    state_detail_activity: Optional[StateDetailActivity] = field(
        default=None,
        metadata={
            "name": "StateDetailActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tubular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    optimum: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Optimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    productive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Productive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    item_state: Optional[ItemState] = field(
        default=None,
        metadata={
            "name": "ItemState",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    proprietary_code: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
