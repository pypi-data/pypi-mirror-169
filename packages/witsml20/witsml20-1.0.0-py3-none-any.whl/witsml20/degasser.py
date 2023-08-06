from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.area_measure import AreaMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.name_tag import NameTag
from witsml20.pressure_measure import PressureMeasure
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Degasser:
    """
    Rig Degasser Schema.

    :ivar manufacturer: Manufacturer or supplier of the item.
    :ivar model: Manufacturer's designated model.
    :ivar dtim_install: Date and time the degasser was installed.
    :ivar dtim_remove: Date and time the degasser was removed.
    :ivar type: Description for the type of object.
    :ivar owner: Contractor/owner.
    :ivar height: Height of the separator.
    :ivar len: Length of the separator.
    :ivar id: Internal diameter of the object.
    :ivar cap_flow: Maximum pump rate at which the unit efficiently
        operates.
    :ivar area_separator_flow: Flow area of the separator.
    :ivar ht_mud_seal: Depth of trip-tank fluid level to provide back
        pressure against the separator flow.
    :ivar id_inlet: Internal diameter of the inlet line.
    :ivar id_vent_line: Internal diameter of the vent line.
    :ivar len_vent_line: Length of the vent line.
    :ivar cap_gas_sep: Safe gas-separating capacity.
    :ivar cap_blowdown: Gas vent rate at which the vent line pressure
        drop exceeds the hydrostatic head because of the mud seal.
    :ivar pres_rating: Pressure rating of the item.
    :ivar temp_rating: Temperature rating of the separator.
    :ivar name_tag: An identification tag for the degasser. A serial
        number is a type of identification tag; however, some tags
        contain many pieces of information.This element only identifies
        the tag and does not describe the contents.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of degasser
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
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    height: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Height",
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
        }
    )
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cap_flow: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CapFlow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    area_separator_flow: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "AreaSeparatorFlow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_mud_seal: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtMudSeal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_inlet: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdInlet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_vent_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdVentLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_vent_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenVentLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cap_gas_sep: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CapGasSep",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cap_blowdown: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CapBlowdown",
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
    temp_rating: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempRating",
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
