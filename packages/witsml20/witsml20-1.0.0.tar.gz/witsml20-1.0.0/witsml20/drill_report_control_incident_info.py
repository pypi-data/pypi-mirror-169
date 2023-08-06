from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.drill_activity_code import DrillActivityCode
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.object_alias import ObjectAlias
from witsml20.pressure_measure import PressureMeasure
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.well_control_incident_type import WellControlIncidentType
from witsml20.well_killing_procedure_type import WellKillingProcedureType
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportControlIncidentInfo:
    """
    Information about a well control incident that occurred during the drill
    report period.

    :ivar dtim: Date and time of the well control incident.
    :ivar md_inflow: The measured depth to the well inflow entry point.
    :ivar tvd_inflow: The true vertical depth to the well inflow entry
        point.
    :ivar phase: Phase is large activity classification, e.g. drill
        surface hole.
    :ivar activity_code: A code used to define rig activity.
    :ivar detail_activity: Custom string to further define an activity.
    :ivar etim_lost: The amount of time lost because of the well control
        incident. Commonly specified in hours.
    :ivar dtim_regained: The date and time at which control of the well
        was regained.
    :ivar dia_bit: The drill bit nominal outside diameter at the time of
        the well control incident.
    :ivar md_bit: The measured depth of the bit at the time of the the
        well control incident.
    :ivar wt_mud: The density of the drilling fluid at the time of the
        well control incident.
    :ivar pore_pressure: The equivalent mud weight value of the pore
        pressure reading.
    :ivar dia_csg_last: Diameter of the last installed casing.
    :ivar md_csg_last: Measured depth of the last casing joint.
    :ivar vol_mud_gained: The gained volume of drilling fluid due to the
        well kick.
    :ivar pres_shut_in_casing: The shut in casing pressure.
    :ivar pres_shut_in_drill: The actual pressure in the drill pipe when
        the rams were closed around it.
    :ivar incident_type: The type of well control incident.
    :ivar killing_type: The type of procedure used to kill the well.
    :ivar formation: The lithological description of the geological
        formation at the incident depth.
    :ivar temp_bottom: The temperature at the bottom of the wellbore.
    :ivar pres_max_choke: The maximum pressure that the choke valve can
        be exposed to.
    :ivar description: A description of the well control incident.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar proprietary_code:
    :ivar uid: Unique identifier for this instance of
        DrillReportControlIncidentInfo.
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
    md_inflow: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdInflow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_inflow: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdInflow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    activity_code: Optional[DrillActivityCode] = field(
        default=None,
        metadata={
            "name": "ActivityCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    detail_activity: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    etim_lost: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimLost",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_regained: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRegained",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dia_bit: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_bit: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_mud: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WtMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pore_pressure: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PorePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    dia_csg_last: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaCsgLast",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_csg_last: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdCsgLast",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_gained: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudGained",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_shut_in_casing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresShutInCasing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_shut_in_drill: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresShutInDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incident_type: Optional[WellControlIncidentType] = field(
        default=None,
        metadata={
            "name": "IncidentType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    killing_type: Optional[WellKillingProcedureType] = field(
        default=None,
        metadata={
            "name": "KillingType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    formation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    temp_bottom: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_max_choke: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresMaxChoke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    proprietary_code: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryCode",
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
