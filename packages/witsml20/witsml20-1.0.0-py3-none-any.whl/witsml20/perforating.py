from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.mass_measure import MassMeasure
from witsml20.mass_per_mass_measure import MassPerMassMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.perf_conveyance_method import PerfConveyanceMethod
from witsml20.pressure_measure import PressureMeasure
from witsml20.reciprocal_length_measure import ReciprocalLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Perforating:
    """
    Information on the perforating job.

    :ivar stage_number: index number of stage
    :ivar bottom_packer_set: Perf-Bottom of packer set depth
    :ivar perforation_fluid_type: Perforation fluid type
    :ivar hydrostatic_pressure: hydrostaticPressure
    :ivar surface_pressure: Surface pressure
    :ivar reservoir_pressure: Reservoir pressure
    :ivar fluid_density: The density of fluid
    :ivar fluid_level: Fluid level.
    :ivar conveyance_method: The conveyance method
    :ivar shots_planned: Number of shots planned
    :ivar shots_density: Number of shots per unit length (ft, m)
    :ivar shots_misfired: The number of missed firings from the gun.
    :ivar orientation: orientaton
    :ivar orientation_method: Description of orientaton method
    :ivar perforation_company: The name of company providing the
        perforation.
    :ivar carrier_manufacturer: The manufacturer of the carrier.
    :ivar carrier_size: Size of the carrier.
    :ivar carrier_description: Description from carrier
    :ivar charge_manufacturer: The manufacturer of the charge.
    :ivar charge_size: The size of the charge.
    :ivar charge_weight: The weight of the charge.
    :ivar charge_type: The type of the charge.
    :ivar ref_log: Reference to the log
    :ivar gun_centralized: True if centralized, else decentralized.
    :ivar gun_size: The size of the perforation gun.
    :ivar gun_desciption: Description about the perforating gun.
    :ivar gun_left_in_hole: Flag indicating whether the gun is left in
        hole or not.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Perforating
    """
    stage_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StageNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bottom_packer_set: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "BottomPackerSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_fluid_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PerforationFluidType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    hydrostatic_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "HydrostaticPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    surface_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "SurfacePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reservoir_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "ReservoirPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_density: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "FluidDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_level: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "FluidLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    conveyance_method: Optional[PerfConveyanceMethod] = field(
        default=None,
        metadata={
            "name": "ConveyanceMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    shots_planned: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShotsPlanned",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    shots_density: Optional[ReciprocalLengthMeasure] = field(
        default=None,
        metadata={
            "name": "ShotsDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    shots_misfired: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShotsMisfired",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    orientation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    orientation_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrientationMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    perforation_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "PerforationCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    carrier_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierManufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    carrier_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CarrierSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    carrier_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    charge_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChargeManufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    charge_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    charge_weight: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    charge_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChargeType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    ref_log: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefLog",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    gun_centralized: Optional[str] = field(
        default=None,
        metadata={
            "name": "GunCentralized",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    gun_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "GunSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gun_desciption: Optional[str] = field(
        default=None,
        metadata={
            "name": "GunDesciption",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    gun_left_in_hole: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GunLeftInHole",
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
