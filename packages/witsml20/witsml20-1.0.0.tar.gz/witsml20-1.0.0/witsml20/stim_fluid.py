from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.dynamic_viscosity_measure import DynamicViscosityMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.stim_fluid_kind import StimFluidKind
from witsml20.stim_fluid_subtype import StimFluidSubtype
from witsml20.stim_material_quantity import StimMaterialQuantity
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimFluid:
    """
    The characteristics and recipe of the stimulation fluid without proppant.

    :ivar name: The name of the fluid.
    :ivar kind: The fluid types.
    :ivar subtype: The fluid subtypes.
    :ivar purpose: The purpose of the fluid.
    :ivar description: The description of the fluid.
    :ivar supplier: The supplier of the fluid.
    :ivar is_kill_fluid: Is the fluid a kill fluid? Values are "true"
        (or "1") and "false" (or "0").
    :ivar volume: Volume of fluid.
    :ivar density: The density of the fluid.
    :ivar fluid_temp: The temperature of the fluid at surface.
    :ivar gel_strength10_min: The shear stress measured at low shear
        rate after a mud has set quiescently for 10 minutes.
    :ivar gel_strength10_sec: The shear stress measured at low shear
        rate after a mud has set quiescently for 10 seconds.
    :ivar specific_gravity: The specific gravity of the fluid at
        surface.
    :ivar viscosity: Viscosity of stimulation fluid.
    :ivar p_h: The pH of the fluid.
    :ivar additive_concentration:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    kind: Optional[StimFluidKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    subtype: Optional[StimFluidSubtype] = field(
        default=None,
        metadata={
            "name": "Subtype",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    is_kill_fluid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsKillFluid",
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
    density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_temp: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FluidTemp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel_strength10_min: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "GelStrength10Min",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel_strength10_sec: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "GelStrength10Sec",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    specific_gravity: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "SpecificGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "Viscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    p_h: Optional[float] = field(
        default=None,
        metadata={
            "name": "pH",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    additive_concentration: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "AdditiveConcentration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
