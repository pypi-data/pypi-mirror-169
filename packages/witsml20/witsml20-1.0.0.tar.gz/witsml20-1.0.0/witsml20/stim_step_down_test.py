from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.stim_pump_flow_back_test_step import StimPumpFlowBackTestStep

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimStepDownTest:
    """
    Diagnostic test involving flowing a well back after treatment.

    :ivar initial_shutin_pres: The initial shutin pressure.
    :ivar bottomhole_fluid_density: The density of the fluid at the
        bottom of the hole adjusting for bottomhole temperature and
        pressure during the step-down test.
    :ivar diameter_entry_hole: Diameter of the injection point or
        perforation.
    :ivar perforation_count: The number of perforations in the interval
        being tested.
    :ivar discharge_coefficient: A coefficient used in the equation for
        calculation of the pressure drop across a perforation set.
    :ivar effective_perfs: The number of perforations in the interval
        being tested that are  calculated to be open to injection, which
        is determined during the step-down test.
    :ivar step: The data related to a particular step in the step-down
        test.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of StimStepDownTest
    """
    initial_shutin_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "InitialShutinPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bottomhole_fluid_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeFluidDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    diameter_entry_hole: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiameterEntryHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerforationCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    discharge_coefficient: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "DischargeCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    effective_perfs: Optional[int] = field(
        default=None,
        metadata={
            "name": "EffectivePerfs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    step: List[StimPumpFlowBackTestStep] = field(
        default_factory=list,
        metadata={
            "name": "Step",
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
