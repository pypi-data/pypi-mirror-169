from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.permeability_length_measure import PermeabilityLengthMeasure
from witsml20.permeability_rock_measure import PermeabilityRockMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimIso135035Point:
    """
    A stress, conductivity, permeability, and temperature data point.

    :ivar conductivity: The conductivity under stress.
    :ivar temperature: The temperature at the time measurements were
        taken.
    :ivar permeability: The permeability under stress.
    :ivar stress: The amount of stress applied.
    :ivar uid: Unique identifier for this instance of
        StimISO13503_5Point
    """
    class Meta:
        name = "StimISO13503_5Point"

    conductivity: Optional[PermeabilityLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    permeability: Optional[PermeabilityRockMeasure] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    stress: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Stress",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
