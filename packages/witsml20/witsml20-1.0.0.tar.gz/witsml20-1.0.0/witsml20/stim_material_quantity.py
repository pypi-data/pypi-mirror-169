from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.mass_measure import MassMeasure
from witsml20.mass_per_time_measure import MassPerTimeMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimMaterialQuantity:
    """
    Stimulation material used.

    :ivar density: The density of material used.
    :ivar mass: The mass of material used.  This should be used without
        specifying any of the other material measures (e.g. volume,
        standard volume, etc.).
    :ivar mass_flow_rate: Rate at which mass of material is flowing.
    :ivar std_volume: The standard volume of material used. Standard
        volume is the volume measured under the same conditions. This
        should be used without specifying any of the other material
        measures (e.g., mass, volume, etc.).
    :ivar volume: The volume of material used.  This should be used
        without specifying any of the other material measures (e.g.
        mass, standard volume, etc.).
    :ivar volume_concentration: The volume per volume measure of
        material used.  This should be used without specifying any of
        the other material measures (e.g. mass, density, standard
        volume, etc.).
    :ivar volumetric_flow_rate: Rate at which the volume of material is
        flowing.
    :ivar material_reference: Material ID is  equal to
        AbstractStimMaterial.RefId. This is a reference to the UID of
        the StimMaterial in the StimJobMaterialCatalog.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        StimMaterialQuantity
    """
    density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mass: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mass_flow_rate: Optional[MassPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MassFlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    std_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StdVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume_concentration: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeConcentration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volumetric_flow_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumetricFlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    material_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterialReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
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
