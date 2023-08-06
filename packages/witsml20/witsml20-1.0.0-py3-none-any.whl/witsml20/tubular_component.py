from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.angle_per_length_measure import AnglePerLengthMeasure
from witsml20.area_measure import AreaMeasure
from witsml20.bend import Bend
from witsml20.bit_record import BitRecord
from witsml20.box_pin_config import BoxPinConfig
from witsml20.connection import Connection
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.force_per_length_measure import ForcePerLengthMeasure
from witsml20.hole_opener import HoleOpener
from witsml20.jar import Jar
from witsml20.length_measure import LengthMeasure
from witsml20.length_per_length_measure import LengthPerLengthMeasure
from witsml20.mass_per_length_measure import MassPerLengthMeasure
from witsml20.material_type import MaterialType
from witsml20.moment_of_force_measure import MomentOfForceMeasure
from witsml20.motor import Motor
from witsml20.mwd_tool import MwdTool
from witsml20.name_tag import NameTag
from witsml20.nozzle import Nozzle
from witsml20.pressure_measure import PressureMeasure
from witsml20.rotary_steerable_tool import RotarySteerableTool
from witsml20.stabilizer import Stabilizer
from witsml20.tubular_component_type import TubularComponentType
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularComponent:
    """Tubular Component Schema.

    Captures the order of the components in the XML instance,which is
    significant. The components are listed in the order in which they
    enter the hole. That is, the first component is the bit.

    :ivar type_tubular_component: Connection whose type is tubular
    :ivar sequence: The sequence within which the components entered the
        hole. That is, a sequence number of 1 entered first, 2 entered
        next, etc.
    :ivar description: Description of item and details.
    :ivar id: Internal diameter of object.
    :ivar od: Outside diameter of the body of the item.
    :ivar od_mx: Maximum outside diameter.
    :ivar len: Length of the item.
    :ivar len_joint_av: Average length of the joint for this string.
    :ivar num_joint_stand: Number of joints per stand of tubulars.
    :ivar wt_per_len: Weight per unit length.
    :ivar grade: Material grade for the tubular section.
    :ivar od_drift: Minimum pass through diameter.
    :ivar tens_yield: Yield stress of steel - worn stress.
    :ivar tq_yield: Torque at which yield occurs.
    :ivar stress_fatigue: Fatigue endurance limit.
    :ivar len_fishneck: Fish neck length.
    :ivar id_fishneck: Fish neck inside diameter.
    :ivar od_fishneck: Fish neck outside diameter.
    :ivar disp: Closed end displacement.
    :ivar pres_burst: Burst pressure.
    :ivar pres_collapse: Collapse pressure.
    :ivar class_service: Service class.
    :ivar wear_wall: Wall thickness wear (commonly in percent).
    :ivar thick_wall: Wall thickness.
    :ivar config_con: Box/Pin configuration.
    :ivar bend_stiffness: Bending stiffness of tubular.
    :ivar axial_stiffness: Axial stiffness of tubular.
    :ivar torsional_stiffness: Torsional stiffness of tubular.
    :ivar type_material: Type of material.
    :ivar dogleg_mx: Maximum dogleg severity.
    :ivar vendor: Name of vendor.
    :ivar model: Component name from manufacturer.
    :ivar name_tag: An identification tag for the component tool. A
        serial number is a type of identification tag; however, some
        tags contain many pieces of information. This element only
        identifies the tag; it does not describe the contents.
    :ivar area_nozzle_flow: Total area of nozzles.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar connection:
    :ivar jar:
    :ivar mwd_tool:
    :ivar bit_record:
    :ivar motor:
    :ivar stabilizer:
    :ivar bend:
    :ivar hole_opener:
    :ivar rotary_steerable_tool:
    :ivar extension_any:
    :ivar nozzle:
    :ivar uid: Unique identifier for this instance of TubularComponent
    """
    type_tubular_component: Optional[TubularComponentType] = field(
        default=None,
        metadata={
            "name": "TypeTubularComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    od_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Len",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    len_joint_av: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenJointAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_joint_stand: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumJointStand",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_per_len: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WtPerLen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Grade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    od_drift: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdDrift",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tens_yield: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "TensYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_yield: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stress_fatigue: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StressFatigue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Disp",
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
    pres_collapse: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCollapse",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    class_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassService",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    wear_wall: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WearWall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    thick_wall: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickWall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    config_con: Optional[BoxPinConfig] = field(
        default=None,
        metadata={
            "name": "ConfigCon",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "BendStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    axial_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "AxialStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    torsional_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "TorsionalStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_material: Optional[MaterialType] = field(
        default=None,
        metadata={
            "name": "TypeMaterial",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dogleg_mx: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "DoglegMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    name_tag: List[NameTag] = field(
        default_factory=list,
        metadata={
            "name": "NameTag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    area_nozzle_flow: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "AreaNozzleFlow",
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
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    jar: Optional[Jar] = field(
        default=None,
        metadata={
            "name": "Jar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mwd_tool: Optional[MwdTool] = field(
        default=None,
        metadata={
            "name": "MwdTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bit_record: Optional[BitRecord] = field(
        default=None,
        metadata={
            "name": "BitRecord",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    motor: Optional[Motor] = field(
        default=None,
        metadata={
            "name": "Motor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stabilizer: List[Stabilizer] = field(
        default_factory=list,
        metadata={
            "name": "Stabilizer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend: List[Bend] = field(
        default_factory=list,
        metadata={
            "name": "Bend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_opener: Optional[HoleOpener] = field(
        default=None,
        metadata={
            "name": "HoleOpener",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rotary_steerable_tool: Optional[RotarySteerableTool] = field(
        default=None,
        metadata={
            "name": "RotarySteerableTool",
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
    nozzle: List[Nozzle] = field(
        default_factory=list,
        metadata={
            "name": "Nozzle",
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
