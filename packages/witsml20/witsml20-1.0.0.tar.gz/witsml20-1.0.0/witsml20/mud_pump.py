from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.angular_velocity_measure import AngularVelocityMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.name_tag import NameTag
from witsml20.power_measure import PowerMeasure
from witsml20.power_per_power_measure import PowerPerPowerMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.pump_type import PumpType
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudPump:
    """
    Rig Mud Pump Schema.

    :ivar index: Relative pump number. One-based.
    :ivar manufacturer: Manufacturer or supplier of the item.
    :ivar model: Manufacturer's designated model.
    :ivar dtim_install: Date and time the pump was installed.
    :ivar dtim_remove: Date and time the pump was removed.
    :ivar owner: Contractor/owner.
    :ivar type_pump: Pump type reference list.
    :ivar num_cyl: Number of cylinders (3 = single acting, 2 = double
        acting)
    :ivar od_rod: Rod outer diameter.
    :ivar id_liner: Inner diameter of the pump liner.
    :ivar pump_action: Pump action. 1 = single acting, 2 = double
        acting.
    :ivar eff: Efficiency of the pump.
    :ivar len_stroke: Stroke length.
    :ivar pres_mx: Maximum pump pressure.
    :ivar pow_hyd_mx: Maximum hydraulics horsepower.
    :ivar spm_mx: Maximum speed.
    :ivar displacement: Pump displacement.
    :ivar pres_damp: Pulsation dampener pressure.
    :ivar vol_damp: Pulsation dampener volume.
    :ivar pow_mech_mx: Maximum mechanical power.
    :ivar name_tag: An identification tag for the pump. A serial number
        is a type of identification tag; however, some tags contain many
        pieces of information.This element onlyidentifies the tag and
        does not describe the contents.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of MudPump.
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
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
    dtim_install: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimInstall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_remove: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRemove",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type_pump: Optional[PumpType] = field(
        default=None,
        metadata={
            "name": "TypePump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_cyl: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumCyl",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_rod: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdRod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_liner: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdLiner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pump_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "PumpAction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+",
        }
    )
    eff: Optional[PowerPerPowerMeasure] = field(
        default=None,
        metadata={
            "name": "Eff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_stroke: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenStroke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_mx: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pow_hyd_mx: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "PowHydMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    spm_mx: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "SpmMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    displacement: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Displacement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pres_damp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresDamp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_damp: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolDamp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pow_mech_mx: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "PowMechMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
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
