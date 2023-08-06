from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml20.equipment_connection import EquipmentConnection
from witsml20.equipment_type import EquipmentType
from witsml20.event_info import EventInfo
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.force_measure import ForceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.object_sequence import ObjectSequence
from witsml20.pressure_measure import PressureMeasure
from witsml20.reference_container import ReferenceContainer
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Assembly:
    """
    Container element for assemblies, or a collection of all assembly
    information.
    """
    part: List["StringEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "Part",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )


@dataclass
class StringEquipment:
    """
    Information regarding equipment that composes (makes up) a string.

    :ivar equipment_type: The type of the equipment. See enumerated
        values.
    :ivar name: The name of the equipment.
    :ivar equipment_event_history: History of events related to this
        equipment.
    :ivar status: The status of the piece of equipment.
    :ivar run_no: The well run number.
    :ivar previous_run_days: The days that the equipment has run.
    :ivar object_condition: Object condition at installation.
    :ivar surface_condition: Object surface condition.
    :ivar count: The count number of the same equipment. The default is
        1.  In some cases, multiple pieces group into one component.
    :ivar length: The total length of the equipment.  This is NOT length
        per unit. This is the length of unit stored at equipmentset's
        equipment information section.
    :ivar md_interval: Measured depth interval in which the equipment is
        installed in the string.
    :ivar tvd_interval: True vertical depth interval in which the
        equipment is installed in the string.
    :ivar outside_string: Flag indicating whether this component is
        inside the string or not .
    :ivar tensile_max: Max tensile strength.
    :ivar pres_rating: Pressure  rating.
    :ivar pres_collapse: Collapse pressure.
    :ivar pres_burst: Burst pressure.
    :ivar heat_rating: Heat rating.
    :ivar is_lineto_surface: Flag indicating the equipment has a line
        connected to the surface.
    :ivar is_centralized: Flag indicating equipment is centralized.
    :ivar has_scratchers: Flag indicating scratchers have been added to
        the equipment.
    :ivar perforation_set_ref_id: Reference to the perforated hole in
        the equipment after a perforation event.
    :ivar permanent_remarks: Remarks on the equipment stored
        permanently.
    :ivar usage_comment: Remarks on the usage of this equipment.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar assembly:
    :ivar order_of_object:
    :ivar inside_component:
    :ivar outside_component:
    :ivar connection_next:
    :ivar uid: Unique identifier for this instance of StringEquipment.
    :ivar equipment_reference_uid: Reference to a piece of equipment.
    """
    equipment_type: Optional[Union[EquipmentType, str]] = field(
        default=None,
        metadata={
            "name": "EquipmentType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".*:.*",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    equipment_event_history: List[EventInfo] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentEventHistory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    run_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunNo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    previous_run_days: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PreviousRunDays",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    object_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    surface_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "TvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    outside_string: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutsideString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tensile_max: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "TensileMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_collapse: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCollapse",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_burst: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBurst",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    heat_rating: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "HeatRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    is_lineto_surface: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLinetoSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    is_centralized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCentralized",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    has_scratchers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasScratchers",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set_ref_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PerforationSetRefId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    permanent_remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "PermanentRemarks",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    usage_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsageComment",
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
    assembly: Optional[Assembly] = field(
        default=None,
        metadata={
            "name": "Assembly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    order_of_object: Optional[ObjectSequence] = field(
        default=None,
        metadata={
            "name": "OrderOfObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    inside_component: List[ReferenceContainer] = field(
        default_factory=list,
        metadata={
            "name": "InsideComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    outside_component: List[ReferenceContainer] = field(
        default_factory=list,
        metadata={
            "name": "OutsideComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    connection_next: List[EquipmentConnection] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionNext",
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
    equipment_reference_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "equipmentReferenceUid",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
