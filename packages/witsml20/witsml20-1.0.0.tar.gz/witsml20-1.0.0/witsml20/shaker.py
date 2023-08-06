from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.name_tag import NameTag
from witsml20.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Shaker:
    """
    Rig Shaker Schema.

    :ivar name: Human-recognizable context for the shaker.
    :ivar manufacturer: Manufacturer or supplier of the item.
    :ivar model: Manufacturer's designated model.
    :ivar dtim_install: Date and time the shaker was installed.
    :ivar dtim_remove: Date and time the shaker was removed.
    :ivar type: Description for the type of object.
    :ivar location_shaker: Shaker location on the rig.
    :ivar num_decks: Number of decks.
    :ivar num_casc_level: Number of cascade levels.
    :ivar mud_cleaner: Is part of mud-cleaning assembly as opposed to
        discrete shale shaker? Values are "true" (or "1") and "false"
        (or "0").
    :ivar cap_flow: Maximum pump rate at which the unit efficiently
        operates.
    :ivar owner: Contractor/owner.
    :ivar size_mesh_mn: Minimum mesh size.
    :ivar name_tag: An identification tag for the shaker. A serial
        number is a type of identification tag; however, some tags
        contain many pieces of information. This element only identifies
        the tag and does not describe the contents. .
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Shaker.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
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
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    location_shaker: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationShaker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_decks: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumDecks",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_casc_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumCascLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_cleaner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MudCleaner",
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
    owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    size_mesh_mn: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMeshMn",
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
