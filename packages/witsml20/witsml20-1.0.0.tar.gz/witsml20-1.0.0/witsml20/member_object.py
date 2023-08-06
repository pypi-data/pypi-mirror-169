from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.generic_measure import GenericMeasure
from witsml20.log_index_type import LogIndexType
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.object_sequence import ObjectSequence

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MemberObject:
    """
    Defines a member of an objectGroup.

    :ivar index_type: For a log object, this specifies the kind of the
        index curve for the log. This is only relevant for a
        systematically growing object.
    :ivar range_min: The minimum growing-object index value that applies
        to this group. The significance of this range is defined by the
        groupType.
    :ivar range_max: The maximum growing-object index value that applies
        to this group. The significance of this range is defined by the
        groupType.
    :ivar range_date_time_min: The minimum log date-time index value
        that applies to this group. The significance of this range is
        defined by the groupType.
    :ivar range_date_time_max: The maximum log date-time index value
        that applies to this group. The significance of this range is
        defined by the groupType.
    :ivar mnemonic_list: A comma delimited list of log curve mnemonics.
        Each mnemonic should only occur once in the list. If not
        specified then the group applies to all curves in the log.
    :ivar reference_depth: A measured depth related to this group. This
        does not necessarily represent an actual depth within a growing-
        object. The significance of this depth is defined by the
        groupType.
    :ivar reference_date_time: A date and time related to this group.
        This does not necessarily represent an actual index within a
        growing-object. The significance of this time is defined by the
        groupType.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar sequence3:
    :ivar object_reference:
    :ivar sequence1:
    :ivar sequence2:
    :ivar uid: Unique identifier for this instance of MemberObject
    """
    index_type: Optional[LogIndexType] = field(
        default=None,
        metadata={
            "name": "IndexType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    range_min: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "RangeMin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    range_max: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "RangeMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    range_date_time_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "RangeDateTimeMin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    range_date_time_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "RangeDateTimeMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    mnemonic_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "MnemonicList",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reference_depth: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "ReferenceDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reference_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
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
    sequence3: Optional[ObjectSequence] = field(
        default=None,
        metadata={
            "name": "Sequence3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    object_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sequence1: Optional[ObjectSequence] = field(
        default=None,
        metadata={
            "name": "Sequence1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sequence2: Optional[ObjectSequence] = field(
        default=None,
        metadata={
            "name": "Sequence2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
