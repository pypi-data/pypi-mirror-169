from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_mass_measure import MassPerMassMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.md_interval import MdInterval
from witsml20.pressure_measure import PressureMeasure
from witsml20.tvd_interval import TvdInterval
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure
from witsml20.well_test_type import WellTestType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportWellTestInfo:
    """
    General information about a production well test conducted during the drill
    report period.

    :ivar dtim: Date and time that the well test was completed.
    :ivar test_type: The type of well test.
    :ivar test_number: The number of the well test.
    :ivar test_md_interval: Test interval expressed as a measured depth.
    :ivar test_tvd_interval: Test interval expressed as a true vertical
        depth.
    :ivar choke_orifice_size: The diameter of the choke opening.
    :ivar density_oil: The density of the produced oil.
    :ivar density_water: The density of the produced water.
    :ivar density_gas: The density of the produced gas.
    :ivar flow_rate_oil: The maximum rate at which oil was produced.
    :ivar flow_rate_water: The maximum rate at which water was produced.
    :ivar flow_rate_gas: The maximum rate at which gas was produced.
    :ivar pres_shut_in: The final shut-in pressure.
    :ivar pres_flowing: The final flowing pressure.
    :ivar pres_bottom: The final bottomhole pressure.
    :ivar gas_oil_ratio: The ratio of the volume of gas to the volume of
        oil.
    :ivar water_oil_ratio: The relative amount of water per amount of
        oil.
    :ivar chloride: The relative amount of chloride in the produced
        water.
    :ivar carbon_dioxide: The relative amount of CO2 gas.
    :ivar hydrogen_sulfide: The relative amount of H2S gas.
    :ivar vol_oil_total: The total amount of oil produced. This includes
        oil that was disposed of (e.g., burned).
    :ivar vol_gas_total: The total amount of gas produced. This includes
        gas that was disposed of (e.g., burned).
    :ivar vol_water_total: The total amount of water produced. This
        includes water that was disposed of.
    :ivar vol_oil_stored: The total amount of produced oil that was
        stored.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportWellTestInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    test_type: Optional[WellTestType] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    test_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "TestNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    test_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "TestMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    test_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "TestTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    choke_orifice_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChokeOrificeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    density_oil: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    density_water: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    density_gas: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flow_rate_oil: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRateOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flow_rate_water: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRateWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flow_rate_gas: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRateGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_shut_in: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresShutIn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_flowing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresFlowing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_bottom: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_oil_ratio: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasOilRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    water_oil_ratio: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterOilRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    chloride: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Chloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    carbon_dioxide: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hydrogen_sulfide: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "HydrogenSulfide",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_oil_total: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolOilTotal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_gas_total: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolGasTotal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_water_total: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolWaterTotal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_oil_stored: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolOilStored",
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
