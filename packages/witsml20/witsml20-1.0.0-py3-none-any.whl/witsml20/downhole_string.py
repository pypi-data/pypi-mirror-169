from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.custom_data import CustomData
from witsml20.data_object_reference import DataObjectReference
from witsml20.downhole_string_type import DownholeStringType
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.string_accessory import StringAccessory
from witsml20.string_equipment_set import StringEquipmentSet
from witsml20.sub_string_type import SubStringType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeString:
    """A section of the downhole component equipment.

    Strings in the completion including casing, tubing, and rod strings
    .A completion may have multiple sets of strings, which may be nested
    each inside another, or run in parallel as in dual string
    completions; all strings are contained in a parent wellbore. Each
    string is composed of equipment, and may also contain accessories
    and/or assemblies.

    :ivar string_type: The type of string defined in the  enumeration
        DownholeStringType.
    :ivar sub_string_type: The type of substring which can be
        SurfaceCasing, IntermediaCasing or ProductionCasing.
    :ivar name: The name of the downhole string.
    :ivar string_install_date: The install date of the downhole string.
    :ivar parent_strings_name: The name of parent string.
    :ivar string_md_interval: Measured depth interval between the top
        and the base of the downhole string.
    :ivar axis_offset: The distance from a sibling string.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar accessories:
    :ivar string_equipment_set:
    :ivar extension_any:
    :ivar reference_wellbore:
    :ivar parent_string:
    :ivar uid: Unique identifier for this instance of DownholeString.
    """
    string_type: Optional[DownholeStringType] = field(
        default=None,
        metadata={
            "name": "StringType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sub_string_type: Optional[SubStringType] = field(
        default=None,
        metadata={
            "name": "SubStringType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    string_install_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StringInstallDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    parent_strings_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentStringsName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    string_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "StringMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    axis_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AxisOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    accessories: Optional[StringAccessory] = field(
        default=None,
        metadata={
            "name": "Accessories",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    string_equipment_set: Optional[StringEquipmentSet] = field(
        default=None,
        metadata={
            "name": "StringEquipmentSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_any: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "ExtensionAny",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reference_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReferenceWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    parent_string: Optional["DownholeString"] = field(
        default=None,
        metadata={
            "name": "ParentString",
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
