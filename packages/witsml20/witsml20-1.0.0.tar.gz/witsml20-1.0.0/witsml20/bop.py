from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.bop_component import BopComponent
from witsml20.length_measure import LengthMeasure
from witsml20.name_tag import NameTag
from witsml20.pressure_measure import PressureMeasure
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Bop:
    """
    Rig blowout preventer (BOP) schema.

    :ivar manufacturer: Manufacturer or supplier of the item.
    :ivar model: Manufacturer's designated model.
    :ivar dtim_install: Date and time the BOP was installed.
    :ivar dtim_remove: Date and time of the BOP was removed.
    :ivar name_tag: An identification tag for the blowout preventer. A
        serial number is a type of identification tag; however, some
        tags contain many pieces of information.This element only
        identifies the tag and does not describe the contents.
    :ivar type_connection_bop: Type of connection to the blowout
        preventer.
    :ivar size_connection_bop: Size of the connection to the blowout
        preventer.
    :ivar pres_bop_rating: Maximum pressure rating of the blowout
        preventer.
    :ivar size_bop_sys: Maximum tubulars passable through the blowout
        preventer.
    :ivar rot_bop: Is this a rotating blowout preventer? Values are
        "true" (or "1") and "false" (or "0").
    :ivar id_booster_line: Inner diameter of the booster line.
    :ivar od_booster_line: Outer diameter of the booster line.
    :ivar len_booster_line: Length of the booster line along the riser.
    :ivar id_surf_line: Inner diameter of the surface line.
    :ivar od_surf_line: Outer diameter of the surface line.
    :ivar len_surf_line: Length of the surface line the along riser.
    :ivar id_chk_line: Inner diameter of the choke line.
    :ivar od_chk_line: Outer diameter of the choke line.
    :ivar len_chk_line: Length of the choke line along the riser.
    :ivar id_kill_line: Inner diameter of the kill line.
    :ivar od_kill_line: Outer diameter of the kill line.
    :ivar len_kill_line: Length of the kill line.
    :ivar type_diverter: Diverter description.
    :ivar dia_diverter: Diameter of the diverter.
    :ivar pres_work_diverter: Working rating pressure of the component.
    :ivar accumulator: Type of accumulator/description.
    :ivar cap_acc_fluid: Accumulator fluid capacity.
    :ivar pres_acc_pre_charge: Accumulator pre-charge pressure.
    :ivar vol_acc_pre_charge: Accumulator pre-charge volume
    :ivar pres_acc_op_rating: Accumulator operating pressure rating.
    :ivar type_control_manifold: The blowout preventer control system.
    :ivar desc_control_manifold: Description of the control system.
    :ivar type_choke_manifold: Type of choke manifold.
    :ivar pres_choke_manifold: Choke manifold pressure.
    :ivar bop_component:
    """
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
    name_tag: List[NameTag] = field(
        default_factory=list,
        metadata={
            "name": "NameTag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_connection_bop: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeConnectionBop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    size_connection_bop: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeConnectionBop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_bop_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBopRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    size_bop_sys: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeBopSys",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    rot_bop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RotBop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_booster_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdBoosterLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_booster_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdBoosterLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_booster_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenBoosterLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_surf_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdSurfLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_surf_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdSurfLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_surf_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenSurfLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_chk_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdChkLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_chk_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdChkLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_chk_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenChkLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_kill_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdKillLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_kill_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdKillLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_kill_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenKillLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_diverter: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeDiverter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dia_diverter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaDiverter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_work_diverter: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresWorkDiverter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    accumulator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Accumulator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cap_acc_fluid: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapAccFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_acc_pre_charge: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresAccPreCharge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_acc_pre_charge: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolAccPreCharge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_acc_op_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresAccOpRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_control_manifold: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeControlManifold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    desc_control_manifold: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescControlManifold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    type_choke_manifold: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeChokeManifold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    pres_choke_manifold: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresChokeManifold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bop_component: List[BopComponent] = field(
        default_factory=list,
        metadata={
            "name": "BopComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
