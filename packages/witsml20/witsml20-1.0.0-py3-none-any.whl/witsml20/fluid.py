from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.dynamic_viscosity_measure import DynamicViscosityMeasure
from witsml20.electric_potential_difference_measure import ElectricPotentialDifferenceMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.generic_measure import GenericMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.mass_measure import MassMeasure
from witsml20.mass_per_mass_measure import MassPerMassMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.mud_class import MudType
from witsml20.pressure_measure import PressureMeasure
from witsml20.rheometer import Rheometer
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Fluid:
    """
    Fluid component schema.

    :ivar type: Description for the type of fluid.
    :ivar location_sample: Sample location.
    :ivar dtim: The time when fluid readings were recorded.
    :ivar md: The measured depth where the fluid readings were recorded.
    :ivar tvd: The true vertical depth where the fluid readings were
        recorded.
    :ivar ecd: Equivalent circulating density where fluid reading was
        recorded.
    :ivar kick_tolerance_volume: Assumed kick volume for calculation of
        kick tolerance based on the kick intensity where the fluid
        reading was recorded.
    :ivar kick_tolerance_intensity: Assumed kick density for calculation
        of kick tolerance where the fluid reading was recorded.
    :ivar temp_flow_line: Flow line temperature measurement where the
        fluid reading was recorded.
    :ivar pres_bop_rating: Maximum pressure rating of the blow out
        preventer.
    :ivar mud_class: The class of the drilling fluid.
    :ivar density: Fluid density.
    :ivar vis_funnel: Funnel viscosity in seconds.
    :ivar temp_vis: Funnel viscosity temperature.
    :ivar pv: Plastic viscosity.
    :ivar yp: Yield point (Bingham and Herschel Bulkley models).
    :ivar gel10_sec: Ten-second gels.
    :ivar gel10_min: Ten-minute gels.
    :ivar gel30_min: Thirty-minute gels.
    :ivar filter_cake_ltlp: Filter cake thickness at low (normal)
        temperature and pressure.
    :ivar filtrate_ltlp: API water loss (low temperature and pressure
        mud filtrate measurement) (volume per 30 min).
    :ivar temp_hthp: High temperature high pressure (HTHP) temperature.
    :ivar pres_hthp: High temperature high pressure (HTHP) pressure.
    :ivar filtrate_hthp: High temperature high pressure (HTHP) filtrate
        (volume per 30 min).
    :ivar filter_cake_hthp: High temperature high pressure (HTHP) filter
        cake thickness.
    :ivar solids_pc: Solids percentage from retort.
    :ivar water_pc: Water content percent.
    :ivar oil_pc: Percent oil content from retort.
    :ivar sand_pc: Sand content percent.
    :ivar solids_low_grav_pc: Low gravity solids percent.
    :ivar solids_low_grav: Solids low gravity content.
    :ivar solids_calc_pc: Percent calculated solids content.
    :ivar barite_pc: Barite content percent.
    :ivar lcm: Lost circulation material.
    :ivar mbt: Cation exchange capacity (CEC) of the mud sample as
        measured by methylene blue titration (MBT). NOTE: This is
        temporarily set to be a GenericMeasure with no unit validation,
        pending addition of CEC units to the Energistics UoM spec.
    :ivar ph: Mud pH.
    :ivar temp_ph: Mud pH measurement temperature.
    :ivar pm: Phenolphthalein alkalinity of whole mud.
    :ivar pm_filtrate: Phenolphthalein alkalinity of mud filtrate.
    :ivar mf: Methyl orange alkalinity of filtrate.
    :ivar alkalinity_p1: Mud alkalinity P1 from alternate alkalinity
        method (volume in ml of 0.02N acid to reach the phenolphthalein
        endpoint).
    :ivar alkalinity_p2: Mud alkalinity P2 from alternate alkalinity
        method (volume in ml of 0.02N acid to titrate, the reagent
        mixture to the phenolphthalein endpoint).
    :ivar chloride: Chloride content.
    :ivar calcium: Calcium content.
    :ivar magnesium: Magnesium content.
    :ivar potassium: Potassium content.
    :ivar brine_pc: Percent brine content.
    :ivar brine_density: Density of water phase of NAF.
    :ivar lime: Lime content.
    :ivar elect_stab: Measurement of the emulsion stability and oil-
        wetting capability in oil-based muds.
    :ivar calcium_chloride_pc: Calcium chloride percent.
    :ivar calcium_chloride: Calcium chloride content.
    :ivar company: Name of company.
    :ivar engineer: Engineer name
    :ivar asg: Average specific gravity of solids.
    :ivar solids_hi_grav_pc: Solids high gravity percent.
    :ivar solids_hi_grav: Solids high gravity content.
    :ivar polymer: Polymers present in the mud system.
    :ivar poly_type: Type of polymers present in the mud system.
    :ivar sol_cor_pc: Solids corrected for chloride content percent.
    :ivar oil_ctg: Oil on cuttings.
    :ivar oil_ctg_dry: Oil on dried cuttings.
    :ivar hardness_ca: Total calcium hardness.
    :ivar sulfide: Sulfide content.
    :ivar average_cutting_size: Average size of the drill cuttings.
    :ivar carbonate: Carbonate content.
    :ivar iron: Iron content.
    :ivar metal_recovered: Metal recovered from the wellbore.
    :ivar turbidity: Turbidity units to measure the cloudiness or
        haziness of a fluid.
    :ivar oil_grease: Oil and grease content.
    :ivar salt: Salt content.
    :ivar salt_pc: Salt percent.
    :ivar tct: True crystallization temperature.
    :ivar water_phase_salinity: A factor showing the activity level of
        salt in oil-based mud.
    :ivar whole_mud_calcium: Calcium content in the whole mud sample,
        including oil and water phases.
    :ivar whole_mud_chloride: Chloride content in the whole mud sample,
        including oil and water phases.
    :ivar zinc_oxide: Zinc oxide content.
    :ivar sodium_chloride: Sodium chloride content.
    :ivar sodium_chloride_pc: Sodium chloride percent.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar rheometer:
    :ivar uid: Unique identifier for this instance of Fluid.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    location_sample: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ecd: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Ecd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    kick_tolerance_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "KickToleranceVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    kick_tolerance_intensity: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "KickToleranceIntensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_flow_line: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempFlowLine",
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
        }
    )
    mud_class: Optional[MudType] = field(
        default=None,
        metadata={
            "name": "MudClass",
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
    vis_funnel: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "VisFunnel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_vis: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempVis",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pv: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "Pv",
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
    gel10_sec: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10Sec",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_min: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10Min",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel30_min: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel30Min",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    filter_cake_ltlp: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FilterCakeLtlp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    filtrate_ltlp: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FiltrateLtlp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_hthp: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempHthp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_hthp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresHthp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    filtrate_hthp: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FiltrateHthp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    filter_cake_hthp: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FilterCakeHthp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    water_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    oil_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sand_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SandPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_low_grav_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsLowGravPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_low_grav: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsLowGrav",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_calc_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsCalcPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    barite_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BaritePc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lcm: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Lcm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mbt: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "Mbt",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ph: Optional[float] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_ph: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempPh",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pm: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Pm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pm_filtrate: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PmFiltrate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Mf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    alkalinity_p1: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AlkalinityP1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    alkalinity_p2: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AlkalinityP2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    chloride: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Chloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    calcium: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Calcium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    magnesium: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Magnesium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    potassium: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Potassium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    brine_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BrinePc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    brine_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BrineDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lime: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Lime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    elect_stab: Optional[ElectricPotentialDifferenceMeasure] = field(
        default=None,
        metadata={
            "name": "ElectStab",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    calcium_chloride_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CalciumChloridePc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    calcium_chloride: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CalciumChloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    company: Optional[str] = field(
        default=None,
        metadata={
            "name": "Company",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    engineer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Engineer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    asg: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Asg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_hi_grav_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsHiGravPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    solids_hi_grav: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolidsHiGrav",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    polymer: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Polymer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    poly_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolyType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    sol_cor_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolCorPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    oil_ctg: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "OilCtg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    oil_ctg_dry: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilCtgDry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hardness_ca: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "HardnessCa",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sulfide: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Sulfide",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_cutting_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AverageCuttingSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    carbonate: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Carbonate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    iron: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    metal_recovered: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MetalRecovered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    turbidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Turbidity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    oil_grease: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilGrease",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    salt: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Salt",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    salt_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SaltPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tct: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Tct",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    water_phase_salinity: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterPhaseSalinity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    whole_mud_calcium: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WholeMudCalcium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    whole_mud_chloride: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WholeMudChloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    zinc_oxide: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ZincOxide",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sodium_chloride: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SodiumChloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sodium_chloride_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SodiumChloridePc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
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
