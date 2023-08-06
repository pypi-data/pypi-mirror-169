from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.cement_additive import CementAdditive
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.dynamic_viscosity_measure import DynamicViscosityMeasure
from witsml20.mass_measure import MassMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.md_interval import MdInterval
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.rheometer import Rheometer
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_mass_measure import VolumePerMassMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementingFluid:
    """
    Cementing Fluid Component Schema.

    :ivar etim_transitions: The elapsed time between the development of
        100lbf/100sq ft gel strength and 500lbf/100 sq ft gel strength.
    :ivar etim_zero_gel: The elapsed time from initiation of the static
        portion of the test until the slurry attains a gel strength of
        100lbf/100sq ft.
    :ivar type_fluid: Fluid type: Mud, Wash, Spacer, Slurry.
    :ivar fluid_index: Fluid Index: 1: first fluid pumped (= original
        mud), last - 1 = tail cement, last = displacement mud.
    :ivar desc_fluid: Fluid description.
    :ivar purpose: Purpose description.
    :ivar class_slurry_dry_blend: Slurry class.
    :ivar slurry_placement_interval: Measured depth interval between the
        top and base of the slurry placement.
    :ivar source_water: Water source description.
    :ivar vol_water: Volume of water.
    :ivar vol_cement: Volume of cement.
    :ivar ratio_mix_water: Mix-water ratio.
    :ivar vol_fluid: Fluid/slurry volume.
    :ivar excess_pc: Excess percent.
    :ivar vol_yield: Slurry yield.
    :ivar density: Fluid density.
    :ivar solid_volume_fraction: Equals 1 - Porosity.
    :ivar vol_pumped: Volume pumped.
    :ivar vol_other: Other volume.
    :ivar fluid_rheological_model: Specify one of these models:
        Newtonian, Bingham, Power Law, and Herschel Bulkley.
    :ivar viscosity: Viscosity (if Newtonian model) or plastic viscosity
        (if Bingham model).
    :ivar yp: Yield point (Bingham and Herschel Bulkley models).
    :ivar n: Power Law index (Power Law and Herschel Bulkley models).
    :ivar k: Consistency index (Power Law and Herschel Bulkley models).
    :ivar gel10_sec_reading: Gel reading after 10 seconds.
    :ivar gel10_sec_strength: Gel strength after 10 seconds.
    :ivar gel1_min_reading: Gel reading after 1 minute.
    :ivar gel1_min_strength: Gel strength after 1 minute.
    :ivar gel10_min_reading: Gel reading after 10 minutes.
    :ivar gel10_min_strength: Gel strength after 10 minutes.
    :ivar type_base_fluid: Type of base fluid: fresh water, sea water,
        brine, brackish water.
    :ivar dens_base_fluid: Density of base fluid.
    :ivar dry_blend_name: Name of dry blend.
    :ivar dry_blend_description: Description of dry blend.
    :ivar mass_dry_blend: Mass of dry blend: the blend is made of
        different solid additives: the volume is not constant.
    :ivar dens_dry_blend: Density of dry blend.
    :ivar mass_sack_dry_blend: Weight of a sack of dry blend.
    :ivar foam_used: Foam used?  Values are "true" (or "1") and "false"
        (or "0").
    :ivar type_gas_foam: Gas type used for foam job.
    :ivar vol_gas_foam: Volume of gas used for foam job.
    :ivar ratio_const_gas_method_av: Constant gas ratio method ratio.
    :ivar dens_const_gas_method: Constant gas ratio method: average
        density.
    :ivar ratio_const_gas_method_start: Constant gas ratio method:
        initial method ratio.
    :ivar ratio_const_gas_method_end: Constant gas ratio method: final
        method ratio.
    :ivar dens_const_gas_foam: Constant gas ratio method: average
        density.
    :ivar etim_thickening: Test thickening time.
    :ivar temp_thickening: Test thickening temperature.
    :ivar pres_test_thickening: Test thickening pressure.
    :ivar cons_test_thickening: Test thickening consistency/slurry
        viscosity: Bearden Consistency (Bc) 0 to 100.
    :ivar pc_free_water: Test free water na: = mL/250ML.
    :ivar temp_free_water: Test free water temperature.
    :ivar vol_test_fluid_loss: Test fluid loss.
    :ivar temp_fluid_loss: Test fluid loss temperature.
    :ivar pres_test_fluid_loss: Test fluid loss pressure.
    :ivar time_fluid_loss: Test fluid loss: dehydrating test period,
        used to compute the API fluid loss.
    :ivar vol_apifluid_loss: API fluid loss = 2 * volTestFluidLoss *
        SQRT(30/timefluidloss).
    :ivar etim_compr_stren1: Compressive strength time 1.
    :ivar etim_compr_stren2: Compressive strength time 2.
    :ivar pres_compr_stren1: Compressive strength pressure 1.
    :ivar pres_compr_stren2: Compressive strength pressure 2.
    :ivar temp_compr_stren1: Compressive strength temperature 1.
    :ivar temp_compr_stren2: Compressive strength temperature 2.
    :ivar dens_at_pres: Slurry density at pressure.
    :ivar vol_reserved: Volume reserved.
    :ivar vol_tot_slurry: Total Slurry Volume.
    :ivar cement_additive:
    :ivar rheometer:
    :ivar uid: Unique identifier for this cementing fluid.
    """
    etim_transitions: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimTransitions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_zero_gel: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimZeroGel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    fluid_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FluidIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 1,
        }
    )
    desc_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    class_slurry_dry_blend: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassSlurryDryBlend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    slurry_placement_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "SlurryPlacementInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    source_water: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    vol_water: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_cement: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolCement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ratio_mix_water: Optional[VolumePerMassMeasure] = field(
        default=None,
        metadata={
            "name": "RatioMixWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_fluid: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    excess_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ExcessPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_yield: Optional[VolumePerMassMeasure] = field(
        default=None,
        metadata={
            "name": "VolYield",
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
    solid_volume_fraction: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidVolumeFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_pumped: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolPumped",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_other: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolOther",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_rheological_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "FluidRheologicalModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    yp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Yp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    n: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "N",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    k: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "K",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_sec_reading: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10SecReading",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_sec_strength: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10SecStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel1_min_reading: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Gel1MinReading",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel1_min_strength: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel1MinStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_min_reading: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10MinReading",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_min_strength: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10MinStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_base_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeBaseFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dens_base_fluid: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensBaseFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dry_blend_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DryBlendName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dry_blend_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "DryBlendDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    mass_dry_blend: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassDryBlend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dens_dry_blend: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensDryBlend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mass_sack_dry_blend: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassSackDryBlend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    foam_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FoamUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_gas_foam: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeGasFoam",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    vol_gas_foam: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolGasFoam",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ratio_const_gas_method_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RatioConstGasMethodAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dens_const_gas_method: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensConstGasMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ratio_const_gas_method_start: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RatioConstGasMethodStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ratio_const_gas_method_end: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RatioConstGasMethodEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dens_const_gas_foam: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensConstGasFoam",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_thickening: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimThickening",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_thickening: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempThickening",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_test_thickening: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTestThickening",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cons_test_thickening: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "ConsTestThickening",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pc_free_water: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PcFreeWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_free_water: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempFreeWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_test_fluid_loss: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTestFluidLoss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_fluid_loss: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempFluidLoss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_test_fluid_loss: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTestFluidLoss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    time_fluid_loss: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TimeFluidLoss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_apifluid_loss: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolAPIFluidLoss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_compr_stren1: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimComprStren1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_compr_stren2: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimComprStren2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_compr_stren1: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresComprStren1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_compr_stren2: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresComprStren2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_compr_stren1: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempComprStren1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_compr_stren2: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempComprStren2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dens_at_pres: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensAtPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_reserved: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolReserved",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_tot_slurry: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTotSlurry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cement_additive: List[CementAdditive] = field(
        default_factory=list,
        metadata={
            "name": "CementAdditive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rheometer: List[Rheometer] = field(
        default_factory=list,
        metadata={
            "name": "Rheometer",
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
